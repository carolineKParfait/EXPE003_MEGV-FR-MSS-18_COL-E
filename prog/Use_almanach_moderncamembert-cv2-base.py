from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification

from optparse import OptionParser
import re
import glob
from pathlib import Path
from more_itertools import chunked
import json
import os
import csv
import shutil
import warnings
warnings.simplefilter("ignore")
# TODO: gérer warnings
# from generic_tools import *
from typing import List #sous python 3.7 qui ne supporte pas list[str] directement (c’est un truc introduit avec Python 3.9+)



def get_parser():
    """Returns a command line parser
    Returns:
        OptionParser. The command line parser
    """
    parser = OptionParser()
    parser.add_option("-d", "--data_path", dest="data_path",
                      help="""Chemin vers les fichiers txt (exemple DATA/*)""", type="string", default="../DATA/")
    parser.add_option('-F', '--Force', help='Recalculer les sorties de REN même si déjà faites',
                      action='store_true', default=False)
    return parser


parser = get_parser()
options, _ = parser.parse_args()
path_corpora = options.data_path
print("")
print("-"*40)
print(f"Path corpora : '{path_corpora}'")
print("--> pour spécifier un autre chemin utiliser l'option -d")
print("-"*40)


def lire_fichier(chemin, is_json=False):
    f = open(chemin, encoding='utf-8')
    if is_json == False:
        chaine = f.read()
    else:
        chaine = json.load(f)
    f.close()
    return chaine


def stocker(chemin, contenu, is_json=False, verbose=False):
    if verbose == True:
        print(f"  Output written in {chemin}")
    w = open(chemin, "w",  encoding="utf-8")
    if is_json == False:
        w.write(contenu)
    else:
        w.write(json.dumps(contenu, indent=2, ensure_ascii=False))
    w.close()


# def chunk_text(text: str, chunk_size: int = 1024) -> list[str]:
def chunk_text(text: str, chunk_size: int = 1024) -> List[str]:# python 3.7
    """Splits text into chunks of specified size."""
    chunks = chunked(text.split(), n=chunk_size)
    return [" ".join(chunk) for chunk in chunks]


def dico_resultats(texte, mod_nme):
    mod = ['CATIE-AQ/Moderncamembert_4entities', "Jean-Baptiste/camembert-ner"]

    if mod_nme == mod[0]:
        nlp = pipeline('token-classification', model='CATIE-AQ/Moderncamembert_4entities',
                           tokenizer='CATIE-AQ/Moderncamembert_4entities', aggregation_strategy="simple")
        nlp.max_length = 50000000  # or any large value, as long as you don't run out of RAM

    else:
        tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner")
        model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner")
        nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
        nlp.max_length = 50000000  # or any large value, as long as you don't run out of RAM


    doc = nlp(texte)
    dico_resultats = {}
    i = 0
    for ent in doc:
        print(ent)
        entite = "entite_"+str(i)
        dico_resultats[entite] = {}
        dico_resultats[entite]["label"] = ent["entity_group"]
        dico_resultats[entite]["text"] = ent['word']
        dico_resultats[entite]["jalons"] = [ent['start'], ent['end']]
        i = i+1
    return (dico_resultats)


# def bio_spacy(texte, nlp="") -> list[list]:
def bio_camembert(texte, mod_nme) -> List[str]:
    mod = ['CATIE-AQ/Moderncamembert_4entities', "Jean-Baptiste/camembert-ner"]

    if mod_nme == mod[0]:
        nlp = pipeline('token-classification', model='CATIE-AQ/Moderncamembert_4entities',
                           tokenizer='CATIE-AQ/Moderncamembert_4entities', aggregation_strategy="simple")

    else:
        tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner")
        model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner")
        nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

    doc = nlp(texte)

    liste_bio = []

    for sentence in doc.sentences:
        for token in sentence.tokens:
            if token.ner == 'O':
                tag = 'O'
            else:
                tag = token.ner  # déjà B-XXX ou I-XXX

            liste_bio.append([token.text, tag])

    return liste_bio


if __name__ == "__main__":
    do_json: bool = True
    # long_path_prefix = r"\\?\\"  # pour Windows long path
    # for modele in ["lg"]:
    for modele in ['CATIE-AQ/Moderncamembert_4entities',"Jean-Baptiste/camembert-ner"]:
    # for modele in ["Jean-Baptiste/camembert-ner"]:
        liste_subcorpus = glob.glob(f"{path_corpora}/*")
        # liste_subcorpus = list(Path(path_corpora).glob("*"))
        # print("path_corpora",path_corpora)
        # print("liste_subcorpus",liste_subcorpus)
        # print("os.getcwd()",os.getcwd())
        if len(liste_subcorpus) == 0:
            print(
                f"Pas de dossier trouvé dans {path_corpora}, traitement terminé")
            exit()
        print("Starting with modèle camembert-%s" % modele.split('/')[-1])

        nom_modele = f"{modele.split('/')[-1]}"
        print("_________________________________________________________________")
        print("\n")
        print("_________________________________________________________________")


        for subcorpus in liste_subcorpus:
            print(f"  Processing {subcorpus}")
            # glob pour REF et OCR
            liste_txt = list(Path(subcorpus).glob("*_REF/*.txt"))
            liste_txt += list(Path(subcorpus).glob("*OCR/*/*.txt"))

            print("  nombre de fichiers txt trouvés :", len(liste_txt))
            print("_________________________________________________________________")

            for path in liste_txt:
                path = Path(path).resolve()  # Absolu obligatoire pour Windows long path
                dossiers = path.parent  # dossier parent
                nom_txt = path.name  # nom du fichier

                # dossier NER
                path_ner = dossiers / f"NER-{nom_modele}"
                path_ner.mkdir(parents=True, exist_ok=True)
                abs_path_ner = str(path_ner.resolve())  # absolu pour \\?\
                print("path_ner :", abs_path_ner)

                # chemins fichiers de sortie
                base_path = Path(abs_path_ner)

                path_output = base_path / f"{nom_txt}_{nom_modele}.json"
                path_output_bio = base_path / f"{nom_txt}_{nom_modele}.bio"
                # path_output = Path(long_path_prefix + abs_path_ner) / f"{nom_txt}_{nom_modele}-{stanza.__version__}.json"
                # path_output_bio = Path(
                #     long_path_prefix + abs_path_ner) / f"{nom_txt}_{nom_modele}-{stanza.__version__}.bio"

                print("path_output :", path_output)
                print("path_output_bio :", path_output_bio)

                # lecture du fichier
                texte = lire_fichier(path)

                # stockage JSON
                if os.path.exists(path_output):
                    if options.Force:
                        print("  Recomputing :", path_output)
                    else:
                        print("Already DONE : ", path_output)
                        continue

                entites = dico_resultats(texte, modele)
                print(f"****************{entites}")
                with open(path_output, "w", encoding="utf-8") as w:
                    w.write(json.dumps(entites, indent=2, ensure_ascii=False))

                # stockage BIO
                entites_bio = bio_camembert(texte, modele)
                with open(path_output_bio, "w", encoding="utf-8", newline='') as f:
                    writer = csv.writer(f, delimiter=' ', quotechar='"')
                    writer.writerows(entites_bio)










