import glob
from pathlib import Path
from generic_tools import *
from renommage import *


def lire_dico(fichier_json):
    liste_en = []
    for key, value in fichier_json.items():
        for k, v in value.items():
            if k == "text":
                liste_en.append(v)
    return liste_en

path_corpora = f"../DATA/"

for gen_path in glob.glob(path_corpora):
    dico_REN = {}
    print("Chemin du dossier Données : ",gen_path)
    path_output = gen_path.split("/")[1]## 1 REN normale
    print("Nom du dossier Données : ",path_output)

    for path_ocr in glob.glob(f"{gen_path}/*/*OCR/*/*NER*/*.json"):
        p = Path(path_ocr)
        print("Chemin du dossier OCR : ", p)
        sous_corpus = p.parts[2]
        print("Sous-corpus : ", sous_corpus)
        nom_fichier = p.parts[-1].split("_")[0]
        print("Nom du fichier :", nom_fichier)
        version = p.parts[-1]
        version=Path(version.split("_")[-2]).stem
        print("Version : ",version)
        vers_ren = p.parts[-1]
        vers_ren = Path(vers_ren.split("_")[-1]).stem
        print("Version de NER : ",vers_ren)

        renommage_version = nommage(version)
        print("Nommage version : ", renommage_version)


        liste_ner_ocr = []
        data_ocr = lire_fichier(path_ocr)
        print(data_ocr)
        liste_data_ocr = lire_dico(data_ocr)
        print(liste_data_ocr)
        set_data_ocr = set(liste_data_ocr)
        print(set_data_ocr)
        for data in set_data_ocr:
            liste_ner_ocr.append(data+"_"+sous_corpus)
        print(liste_ner_ocr)

        # dico_REN[vers_ren] = {}
        if vers_ren  in dico_REN:
            if renommage_version in dico_REN[vers_ren]:
                dico_tmp = dico_REN[vers_ren][ renommage_version]
                dico_tmp += liste_ner_ocr
                dico_REN[vers_ren][ renommage_version] = dico_tmp
            else:
                dico_REN[vers_ren][ renommage_version] = liste_ner_ocr
        else:
            dico_REN[vers_ren ] = {}
            if renommage_version in dico_REN[vers_ren]:
                dico_tmp=dico_REN[vers_ren][renommage_version]
                dico_tmp+=liste_ner_ocr
                dico_REN[vers_ren][renommage_version]= dico_tmp
            else:
                dico_REN[vers_ren][renommage_version] = liste_ner_ocr

        # print(dico_REN)


    # for path_ref in glob.glob(f"{gen_path}/*/*REF/*NER*/*.json"):
    #     print("Chemin du dossier REF : ", path_ref)
    #     auteur = path_ref.split("/")[2] #4 archéo
    #     # print("****AUTEUR***:",auteur)
    #     version_REN_ref = model_REN(path_ref)
    #     # version_REN_ref = "Ref."
    #     liste_ner_ref = []
    #     data_ref=lire_json(path_ref)
    #     for data in data_ref:
    #         liste_ner_ref.append(data+"_"+auteur)
    #
    #     if version_REN_ref  in dico_REN:
    #         if GT in dico_REN[version_REN_ref]:
    #             dico_tmp = dico_REN[version_REN_ref][ GT]
    #             dico_tmp += liste_ner_ref
    #             dico_REN[version_REN_ref][GT] = dico_tmp
    #         else:
    #             dico_REN[version_REN_ref][GT] = liste_ner_ref
    #     else:
    #         dico_REN[version_REN_ref] = {}
    #         if GT in dico_REN[version_REN_ocr]:
    #             dico_tmp=dico_REN[version_REN_ref][GT]
    #             dico_tmp+=liste_ner_ref
    #             dico_REN[version_REN_ref][GT]= dico_tmp
    #         else:
    #             dico_REN[version_REN_ref][GT] = liste_ner_ref
    # # print(dico_REN["Ref"])
    # for kle, value in dico_REN.items():
    #     if kle != GT :
    #         # print(kle)
    #         value[GT] = {}
    #         value[GT] = dico_REN[version_REN_ref][GT]
    # # print(dico_REN)
    # #
    # for kle, value in dico_REN.items():
    #
    #     stocker(f"../Upsetplot_intersection/GLOBAL/{path_output}/{path_output}_{GT}_{kle}.json" ,value)
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


