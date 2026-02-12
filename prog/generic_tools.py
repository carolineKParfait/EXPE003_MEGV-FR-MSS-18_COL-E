import json
import sklearn
#from sklearn.neighbors import DistanceMetric
from sklearn.metrics import DistanceMetric
from sklearn.feature_extraction.text import CountVectorizer
import warnings
import re
from jiwer import wer
from jiwer import cer
from scipy.stats import entropy
import scipy
from difflib import SequenceMatcher
from pathlib import Path

warnings.simplefilter("ignore")
re_URL = re.compile(r"^\s*URL.*$", re.MULTILINE)
re_TAG = re.compile(r"(<[phl]>)", re.IGNORECASE)
re_WS = re.compile(r"\s+")
re_CTRL = re.compile("[\x00-\x1F]+")
re_HI = re.compile("[\x80-\xFF]+")

def lire_fichier(chemin, is_json=False):
    """
    Lecture de fichiers texte / JSON (Windows + UTF-8)
    """
    try:
        with open(chemin, encoding="utf-8", errors="ignore") as f:
            if not is_json:
                chaine = f.read()
            else:
                chaine = json.load(f)
    except Exception as e:
        print(f"Erreur lecture fichier {chemin} :", e)
        return ""

    # Sécurité : toujours retourner une chaîne exploitable
    if chaine is None:
        return ""

    if isinstance(chaine, str):
        chaine = chaine.strip()
        if not chaine:
            print(f"⚠️ Fichier vide après lecture : {chemin}")
            return ""

    return chaine

def stocker( chemin, contenu, is_json=False, verbose =False):
    if verbose==True:
      print(f"  Output written in {chemin}")
    w = open(chemin, "w")
    if is_json==False:
      w.write(contenu)
    else:
      w.write(json.dumps(contenu , indent = 2, ensure_ascii=False))
    w.close()

def get_distances(texte1, texte2, liste_name =["jaccard", "braycurtis","dice", "cosinus"] ):
    dico = {}
    if type(texte1) is list:
      texte1 = " ".join(texte1)
      texte2 = " ".join(texte2)
    for metric_name in liste_name :
        dico[metric_name] = []
        liste_resultat_dist2 = []
        V = CountVectorizer(ngram_range=(2,3), analyzer='char', stop_words=None, token_pattern=r"(?u)\b\w+\b")
        # V = CountVectorizer(analyzer='word')
        X = V.fit_transform([texte1, texte2]).toarray()
        try:
            X = V.fit_transform([texte1, texte2]).toarray()
        except ValueError:
            print("⚠️ Vocabulaire vide malgré token_pattern")
            return {}
        if metric_name!= "cosinus" :
            dist = DistanceMetric.get_metric(metric_name)
            distance_tab1=dist.pairwise(X)
            liste_resultat_dist2.append(distance_tab1[0][1])
        else:
            distance_tab1=sklearn.metrics.pairwise.cosine_distances(X)
            liste_resultat_dist2.append(distance_tab1[0][1])
        dico[metric_name] = liste_resultat_dist2
    scores2 = get_new_scores(texte1, texte2)
    for mesure_name, res in scores2.items():
      dico[mesure_name]=res
    return dico

##TODO: Fonction provenant de waddle: améliorer l'intégration
def get_new_scores(HYP_text, GT_text):
  scores= {}
  toto = ["precision", "recall", "f-score"]
  tokens_GT = re.findall("[a-zA-ZÀ-ÿ][a-zA-ZÀ-ÿ-]*", HYP_text)
  tokens_DET = re.findall("[a-zA-ZÀ-ÿ][a-zA-ZÀ-ÿ-]*", GT_text)
  GT_abs, GT_rel = get_voc(tokens_GT)
  DET_abs, DET_rel = get_voc(tokens_DET)
  voc_GT = set(GT_abs.keys())
  voc_DET = set(DET_abs.keys())
  dic = {"TP":len(voc_GT.intersection(voc_DET)),
         "FP":len(voc_DET.difference(voc_GT)),
         "FN":len(voc_GT.difference(voc_DET))}
  scores["voc_eval_res"] = {x: get_measures(dic)[x] for x in toto}
  scores["KL_res"] = {"KL divergence":get_Kullback(GT_rel, DET_rel),
                      "Euclidean Dist.":get_euclidean(GT_rel, DET_rel),
                      "WER": wer(" ".join(tokens_GT), " ".join(tokens_DET)),
                      "CER": cer(" ".join(tokens_GT), " ".join(tokens_DET)),
                      "Cosine Dist.":get_cosine(GT_rel, DET_rel)}
  dic2 = occ_eval(GT_abs,DET_abs)
  scores["occ_eval_res"] = {x: get_measures(dic2)[x] for x in toto}
  return scores
def get_voc(tokens):
  d_abs= {}
  for tok in tokens:
    d_abs.setdefault(tok, 0)
    d_abs[tok]+=1
  l = len(tokens)
  d_rel = {x:y/l for x, y in d_abs.items()}
  return d_abs, d_rel

def get_Kullback(dic1, dic2):
  smoothing = 0.00001#si une des probas est zero, KL est infini 
  vec1, vec2 =  dic2vec(dic1, dic2, smoothing)
  return entropy(vec1, qk=vec2)

def get_cosine(dic1, dic2):
  vec1, vec2 =  dic2vec(dic1, dic2, 0)
  return scipy.spatial.distance.cosine(vec1, vec2)

def get_euclidean(dic1, dic2):
  vec1, vec2 =  dic2vec(dic1, dic2, 0)
  return scipy.spatial.distance.euclidean(vec1, vec2)

def get_dice(dic1, dic2):
  vec1, vec2 =  dic2vec(dic1, dic2, 0)
  return scipy.spatial.distance.dice(vec1, vec2)

def dic2vec(dic1, dic2, smoothing=0): #TODO: improve with list comprehension
  L1, L2 = [], []
  for cle1, proba1 in dic1.items():
    L1.append(proba1)
    proba2 = smoothing
    if cle1 in dic2:
      proba2=dic2[cle1]
    L2.append(proba2)
  for cle2, proba2 in dic2.items():
    L2.append(proba2)
    proba1 = smoothing
    if cle2 in dic1:
      proba1 = dic1[cle2]
    L1.append(proba1)
  return L1, L2

def get_measures(dic, beta=1):
  """
  Computing measures from True Positives ....
  """
  TP, FP, FN = dic["TP"], dic["FP"], dic["FN"]
  if TP == 0:
      return {"recall": 0, "precision": 0, "f-score":0}
  R = 100*float(TP)/(TP+FN)
  P = 100*float(TP)/(TP+FP)
  B = beta*beta
  F = (1+B)*P*R/(B*P+R)
  return {"recall": round(R,4),"precision":round(P,4),"f-score": round(F, 4)}

def occ_eval(GT_abs, DET_abs):
  dic = {"TP":0, "FP":0, "FN":0}
  for cle, eff_GT in GT_abs.items():
    eff_DET = 0
    if cle in DET_abs:
      eff_DET = DET_abs[cle]
    FN = max(0, eff_GT-eff_DET)
    FP = max(0, eff_DET-eff_GT)
    dic["FN"] += FN
    dic["FP"] += FP
    dic["TP"] += eff_GT-FN
  for cle, eff_DET in DET_abs.items():
    if cle not in GT_abs:
      dic["FP"]+=eff_DET
  return dic
def evaluate_file(text_file, gold_file):
  import langid
  filename = text_file
  opt_ascii = False
  opt_unlabelled = False
  opt_noheader = True
  opt_total = False
  opt_summary = False
  sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ss = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  text = normalize(slurp_file(text_file), opt_ascii, opt_unlabelled)
  gold = normalize(slurp_file(gold_file), opt_ascii, opt_unlabelled)
  lang = langid.classify(gold)
  text_words = re_WS.split(text)
  gold_words = re_WS.split(gold)
  if lang[0]=="zh":#TODO: correct for tags
    text_words = [x for x in text] 
    gold_words = [x for x in gold]
  alignment = SequenceMatcher(None, text_words, gold_words)
  diff = make_diff(alignment, text_words, gold_words)
  eval_list = evaluate(diff)
  return eval_list
def normalize(text, ascii=False, unlabelled=False):
	text = re_URL.sub("", text)           # remove URL line at start of gold standard files
	text = re_CTRL.sub(" ", text)         # replace any control characters by spaces (includes newlines)

	if unlabelled:
		text = re_TAG.sub("\n<p> ", text) # start each segment on new line, normalise tags
	else:
		text = re_TAG.sub(r"\n\g<1> ", text)  # only break lines before segment markers

	text = re_WS.sub(" ", text)           # normalise whitespace (including line breaks) to single spaces
	if ascii:
		text = re_HI.sub("", text)        # delete non-ASCII characters (to avoid charset problems)

	return text
def slurp_file(filename):
	fh = open(filename, encoding="utf-8")
	body = fh.read()
	fh.close()
	return body
def make_diff(alignment, text_w, gold_w):
	diff = []
	for tag, i1, i2, j1, j2 in alignment.get_opcodes():
		text_region = text_w[i1:i2]
		gold_region = gold_w[j1:j2]
		if tag == "replace":
			diff.append( ("delete", text_region, []) )
			diff.append( ("insert", [], gold_region) )
		else:
			diff.append( (tag, text_region, gold_region) )
	return diff
def evaluate(diff):
	tp = fp = fn = 0
	tag_tp = tag_fp = tag_fn = 0
	for tag, text, gold in diff:
		text_tags = 0
		for i in filter(re_TAG.match, text):text_tags+=1
#		text_tags = len( filter(re_TAG.match, text) )
		gold_tags = 0
		for i in filter(re_TAG.match, gold):gold_tags+=1
#		gold_tags = len( filter(re_TAG.match, gold) )
		text_l = len(text)
		gold_l = len(gold)
		if tag == "delete":
			fp += text_l
			tag_fp += text_tags
		elif tag == "insert":
			fn += gold_l
			tag_fn += gold_tags
		else:
			tp += text_l
			tag_tp += text_tags
			assert text_l == gold_l
			assert text_tags == gold_tags

	n_text = tp + fp if tp + fp > 0 else 1
	n_gold = tp + fn if tp + fn > 0 else 1
	precision = float(tp) / n_text
	recall = float(tp) / n_gold
	precision_plus_recall = precision + recall if precision + recall > 0 else 1
	f_score = 2 * precision * recall / precision_plus_recall

	tags_text = tag_tp + tag_fp if tag_tp + tag_fp > 0 else 1
	tags_gold = tag_tp + tag_fn if tag_tp + tag_fn > 0 else 1
	tag_precision = float(tag_tp) / tags_text
	tag_recall = float(tag_tp) / tags_gold
	precision_plus_recall = tag_precision + tag_recall if tag_precision + tag_recall > 0 else 1
	tag_f_score = 2 * tag_precision * tag_recall / precision_plus_recall

	out = {	"f-score":100 * f_score, "precision":100 * precision, "recall":100 * recall, 
		"tag_f_score":100 * tag_f_score, "tag_precision":100 * tag_precision, "tag_recall":100 * tag_recall, 
		"tp":tp, "fp":fp, "fn":fn, 
		"tag_tp":tag_tp, "tag_fp":tag_fp, "tag_fn":tag_fn}
	return out

def lire_dico(fichier_json):
    liste_en = []
    for key, value in fichier_json.items():
        for k, v in value.items():
            if k == "text":
                liste_en.append(v)
    return liste_en

def infodata(path, typedata = ""):
    p = Path(path)
    # print("Chemin du dossier OCR : ", p)
    sous_corpus = p.parts[2]
    # print("Sous-corpus : ", sous_corpus)
    nom_fichier = p.parts[-1].split("_")[0]
    print("Nom du fichier :", nom_fichier)
    vers_ren = p.parts[-1]
    vers_ren = Path(vers_ren.split("_")[-1]).stem
    # print("Version de NER : ", vers_ren)

    version = None
    if typedata == "OCR":
        version = p.parts[-1]
        version = Path(version.split("_")[-2]).stem
        # print("Version : ", version)
        version = nommage(version)
        # print("Nommage version : ", version)

    else :
        version = "REF"
        # print("Version REF : ",version)
    return sous_corpus, version, vers_ren

def jsonsetlist(path, sous_cpus):
    p = Path(path)
    liste_ner = []
    data = lire_fichier(p, True)
    print(data)
    liste_data = lire_dico(data)
    print(liste_data)
    set_data = set(liste_data)
    print(set_data)
    for data in set_data:
        liste_ner.append(data + "_" + sous_cpus)
    # print(liste_ner)
    return liste_ner

def dico_output(dico_sortie, liste2ner, version2txt, version2ren ):
    if version2ren in dico_sortie:
        if version2txt in dico_sortie[version2ren]:
            dico_tmp = dico_sortie[version2ren][version2txt]
            dico_tmp += liste2ner
            dico_sortie[version2ren][version2txt] = dico_tmp
        else:
            dico_sortie[version2ren][version2txt] = liste2ner
    else:
        dico_sortie[version2ren ] = {}
        if version2txt in dico_sortie[version2ren]:
            dico_tmp=dico_sortie[version2ren][version2txt]
            dico_tmp+=liste2ner
            dico_sortie[version2ren][version2txt]= dico_tmp
        else:
            dico_sortie[version2ren][version2txt] = liste2ner

    return dico_sortie

def nommage(version):

    if version == "fonduegdmegvv2":
        version = re.sub("fonduegdmegvv2", "FoNDUE-GD-MEGV_v2", version)

    return version
