import glob
import json

def lire_json (chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data
def model_ocr(chemin):
    ocr_mod = chemin.split("/")[4]#REN Normale
    # ocr_mod = chemin.split("/")[6]##5 Correction 6 archéo
    ocr_mod = ocr_mod.split("_")[-1]
    # liste_moteur.append(ocr_mod)
    # moteur = set(liste_moteur)
    return ocr_mod

def model_REN(chemin):
    REN_version = chemin.split("_")[-1]
    REN_version = REN_version.split("-liste")[0]
    return REN_version


def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)
    return chemin
liste_GT = ["REF-GOLD", "REF-ACCMAJ", "Kraken-GOLD", "Kraken-ACCMAJ", "Tesseract-GOLD", "Tesseract-ACCMAJ"]
GT = liste_GT[5]
path_corpora = f"../CORPUS_COMPAR_TAL-ENS2_MISLABEL/"
# path_corpora = f"../CORRECTION_DISTANCES/small-*"
# path_corpora = f"../small-*"


for gen_path in glob.glob(path_corpora):
    dico_REN = {}
    print("_____________",gen_path)
    path_output = gen_path.split("/")[1]## 1 REN normale
    print("----------------------------------->>>",path_output)
    paths_ocr= f"{gen_path}*/*VERSIONS/*/NER/*liste.json"
    paths_ref = f"%s*/*{GT}/NER/*liste.json"%gen_path

    for path_ocr in glob.glob(paths_ocr):
        print(path_ocr)
        auteur = path_ocr.split("/")[2] #4 archéo, 2 ou 3 pour autres
        print(auteur)
        version_REN_ocr=model_REN(path_ocr)
        # dico_REN[version_REN_ocr]={}
        moteur_ocr=model_ocr(path_ocr)
        liste_ner_ocr = []
        print(moteur_ocr)
        data_ocr=lire_json(path_ocr)
        # print(data_ocr)
        # data_ocr=set(data_ocr)
        for data in data_ocr:
            liste_ner_ocr.append(data+"_"+auteur)

        if version_REN_ocr  in dico_REN:
            if moteur_ocr in dico_REN[version_REN_ocr]:
                dico_tmp = dico_REN[version_REN_ocr][ moteur_ocr]
                dico_tmp += liste_ner_ocr
                dico_REN[version_REN_ocr][ moteur_ocr] = dico_tmp
            else:
                dico_REN[version_REN_ocr][ moteur_ocr] = liste_ner_ocr
        else:
            dico_REN[version_REN_ocr ] = {}
            if moteur_ocr in dico_REN[version_REN_ocr]:
                dico_tmp=dico_REN[version_REN_ocr][moteur_ocr]
                dico_tmp+=liste_ner_ocr
                dico_REN[version_REN_ocr][moteur_ocr]= dico_tmp
            else:
                dico_REN[version_REN_ocr][moteur_ocr] = liste_ner_ocr

    # print(dico_REN)
    for path_ref in glob.glob(paths_ref):
        # print(path_ref)
        auteur = path_ref.split("/")[2] #4 archéo
        # print("****AUTEUR***:",auteur)
        version_REN_ref = model_REN(path_ref)
        # version_REN_ref = "Ref."
        liste_ner_ref = []
        data_ref=lire_json(path_ref)
        for data in data_ref:
            liste_ner_ref.append(data+"_"+auteur)

        if version_REN_ref  in dico_REN:
            if GT in dico_REN[version_REN_ref]:
                dico_tmp = dico_REN[version_REN_ref][ GT]
                dico_tmp += liste_ner_ref
                dico_REN[version_REN_ref][GT] = dico_tmp
            else:
                dico_REN[version_REN_ref][GT] = liste_ner_ref
        else:
            dico_REN[version_REN_ref] = {}
            if GT in dico_REN[version_REN_ocr]:
                dico_tmp=dico_REN[version_REN_ref][GT]
                dico_tmp+=liste_ner_ref
                dico_REN[version_REN_ref][GT]= dico_tmp
            else:
                dico_REN[version_REN_ref][GT] = liste_ner_ref
    # print(dico_REN["Ref"])
    for kle, value in dico_REN.items():
        if kle != GT :
            # print(kle)
            value[GT] = {}
            value[GT] = dico_REN[version_REN_ref][GT]
    # print(dico_REN)
    #
    for kle, value in dico_REN.items():

        stocker(f"../Upsetplot_intersection/GLOBAL/{path_output}/{path_output}_{GT}_{kle}.json" ,value)
    #     # stocker(f"../Upsetplot_intersection/GLOBAL/{path_output}/{path_output}_{kle}.json", value)
    #     # stocker(f"../CORRECTION_DISTANCES/Upsetplot_intersection/GLOBAL/{path_output}/{path_output}_{kle}.json", value)
    # liste_res_nb = {}
    # for key, dico_resultat in dico_REN.items():
    #     kk=key.split("-")[-1]
    #     # print("kk",kk)
    #     for cle, valeur in dico_resultat.items():
    #         set_valeur = set(valeur)
    #         print(cle)
    #         # print(valeur[:100])
    #         print(len(valeur))
    #         print(len(set(valeur)))
    #         liste_res_nb[key+"_"+cle] = {}
    #         liste_res_nb[key+"_"+cle]["EN-occ"] = len(valeur)
    #         liste_res_nb[key+"_"+cle]["EN-type"] = len(set(valeur))
    #         print(liste_res_nb)
    #
    #     stocker(f"../Upsetplot_intersection/GLOBAL/nombre_entite/{path_output}_{GT}--nb_entite.json",liste_res_nb)
    # #     stocker(f"../Upsetplot_intersection/GLOBAL/nombre_entite/{path_output}--nb_entite.json", liste_res_nb)
    # # stocker(f"../CORRECTION_DISTANCES/Upsetplot_intersection/GLOBAL/nombre_entite/{path_output}--nb_entite.json", liste_res_nb)


