import glob
from generic_tools import *
import os


def chemin_stockage(path) :
    path_output = Path(path)
    path_output.mkdir(parents=True, exist_ok=True)
    return path_output

path_corpora = f"../DATA-COL-E/"

for gen_path in glob.glob(path_corpora):
    dico_REN = {}
    print("Chemin du dossier Données : ",gen_path)

#___________________________GLOBAL_____________________________________
    for path_ocr in glob.glob(f"{gen_path}/*/*OCR/*/*NER*/*.json"):
        metadata_ocr = infodata(path_ocr, "OCR")
        print("Métadonnées des données OCR", metadata_ocr)
        data_ocr = jsonsetlist(path_ocr, metadata_ocr[0])
        print("Liste des données OCR", data_ocr)
        dico_output(dico_REN, data_ocr, metadata_ocr[1],metadata_ocr[2])
        print("______________________________________________")
        print("______________________________________________")
        print("______________________________________________")
        print("______________________________________________")
    print("dictionnaire transitoire", dico_REN)

    for path_ref in glob.glob(f"{gen_path}/*/*REF/*NER*/*.json"):
        p_ref = Path(path_ref)
        metadata_ref = infodata(p_ref, "REF")
        print("Métadonnées des données REF", metadata_ref)
        data_ref = jsonsetlist(p_ref, metadata_ref[0])
        print("Liste des données de REF", data_ref)
        # print(type(data_ref))
        dico_output(dico_REN, data_ref, metadata_ref[1],metadata_ref[2])
        print("______________________________________________")
        print("______________________________________________")
        print("______________________________________________")
        print("______________________________________________")

    print("dictionnaire transitoire", dico_REN)

    # for kle, value in dico_REN.items():
    #     stocker(f"{gen_path}Upsetplot_intersection/GLOBAL/{metadata_ocr[1]}_{kle}.json" ,value, True)
    for kle, value in dico_REN.items():
        nom_fichier = f"{metadata_ocr[1]}_{kle}.json"
        # print("Nom du fichier de sortie : ", nom_fichier)
        chemin_sortie = p_ref.parents[4] / "Upsetplot_intersection" / "GLOBAL"
        print("Chemin de sortie", chemin_sortie)
        print(type(chemin_sortie))
        chemin_stockage(chemin_sortie)
        nom_chemin_sortie = chemin_sortie / nom_fichier
        print("Chemin de sortie et nom du fichier", nom_chemin_sortie)
        #             # stockage JSON
        if nom_chemin_sortie.is_file():  # Vérifie que c'est un vrai fichier
            print("Already DONE : ", nom_chemin_sortie)
            continue
        print("Nom du modèle de langue : ", kle)
        print("Clés du dictionnaire à stocker", value.keys())
        print("Écriture JSON :", nom_chemin_sortie)
        stocker(nom_chemin_sortie, value, True)
#___________________________GLOBAL_____________________________________

# # ___________________________Par SOUS CORPUS____________________________
#     for path_ocr in glob.glob(f"{gen_path}/*/"):
#         # print(path_ocr)
#         dico_REN = {}
#         for file_ocr in glob.glob(f"{path_ocr}/*OCR/*/*NER*/*.json"):
#             p_ocr = Path(file_ocr)
#             metadata_ocr = infodata(p_ocr, "OCR")
#             print("Métadonnées des données OCR", metadata_ocr)
#             data_ocr = jsonsetlist(p_ocr,metadata_ocr[0])
#             print("Liste des données OCR", data_ocr)
#             dico_output(dico_REN, data_ocr, metadata_ocr[1],metadata_ocr[2])
#             print("______________________________________________")
#             print("______________________________________________")
#             print("______________________________________________")
#             print("______________________________________________")
#         #
#         for file_ref in glob.glob(f"{path_files}/*REF/*NER*/*.json"):
#             p_ref = Path(file_ref)
#             metadata_ref = infodata(p_ref, "REF")
#             print("Métadonnées des données REF", metadata_ref)
#             data_ref = jsonsetlist(p_ref,metadata_ocr[0])
#             # print("Liste des données de REF", data_ref)
#             # # print(type(data_ref))
#             dico_output(dico_REN, data_ref, metadata_ref[1],metadata_ref[2])
#             # print("______________________________________________")
#             # print("______________________________________________")
#             # print("______________________________________________")
#             # print("______________________________________________")
#             #
#         for kle, value in dico_REN.items():
#
#             nom_fichier = f"{metadata_ocr[0]}_{metadata_ocr[1]}_{kle}.json"
#             # print("Nom du fichier de sortie : ", nom_fichier)
#             chemin_sortie = p_ref.parents[4] / "Upsetplot_intersection" / "Sous_Corpus"
#             print("Chemin de sortie", chemin_sortie)
#             print(type(chemin_sortie))
#             chemin_stockage(chemin_sortie)
#             nom_chemin_sortie = chemin_sortie / nom_fichier
#             print("Chemin de sortie et nom du fichier", nom_chemin_sortie)
#             #             # stockage JSON
#             if nom_chemin_sortie.is_file():  # Vérifie que c'est un vrai fichier
#                 print("Already DONE : ", nom_chemin_sortie)
#                 continue
#             print("Nom du modèle de langue : ", kle)
#             print("Clés du dictionnaire à stocker", value.keys())
#             print("Écriture JSON :", nom_chemin_sortie)
#             stocker(nom_chemin_sortie, value, True)
#
#
#
# # # ___________________________Par SOUS CORPUS____________________________


## ___________________________A REVOIR____________________________
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


