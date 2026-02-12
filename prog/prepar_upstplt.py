import glob
from generic_tools import *

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
        metadata_ref = infodata(path_ref, "REF")
        print("Métadonnées des données REF", metadata_ref)
        data_ref = jsonsetlist(path_ref, metadata_ref[0])
        print("Liste des données de REF", data_ref)
        # print(type(data_ref))
        dico_output(dico_REN, data_ref, metadata_ref[1],metadata_ref[2])
        print("______________________________________________")
        print("______________________________________________")
        print("______________________________________________")
        print("______________________________________________")

    print("dictionnaire transitoire", dico_REN)

    for kle, value in dico_REN.items():
        stocker(f"{gen_path}Upsetplot_intersection/GLOBAL/{metadata_ocr[1]}_{kle}.json" ,value, True)
#___________________________GLOBAL_____________________________________

# # ___________________________Par SOUS CORPUS____________________________
#     for path_files in glob.glob(f"{gen_path}/*/"):
#         # print(path_ocr)
#         dico_REN = {}
#         for file_ocr in glob.glob(f"{path_files}/*OCR/*/*NER*/*.json"):
#             print(file_ocr)
#             metadata_ocr = infodata(file_ocr, "OCR")
#             print("Métadonnées des données OCR", metadata_ocr)
#             data_ocr = jsonsetlist(file_ocr,metadata_ocr[0])
#             print("Liste des données OCR", data_ocr)
#             dico_output(dico_REN, data_ocr, metadata_ocr[1],metadata_ocr[2])
#             print("______________________________________________")
#             print("______________________________________________")
#             print("______________________________________________")
#             print("______________________________________________")
#
#         for file_ref in glob.glob(f"{path_files}/*REF/*NER*/*.json"):
#             metadata_ref = infodata(file_ref, "REF")
#             print("Métadonnées des données REF", metadata_ref)
#             data_ref = jsonsetlist(file_ref,metadata_ocr[0])
#             print("Liste des données de REF", data_ref)
#             # print(type(data_ref))
#             dico_output(dico_REN, data_ref, metadata_ref[1],metadata_ref[2])
#             print("______________________________________________")
#             print("______________________________________________")
#             print("______________________________________________")
#             print("______________________________________________")
#
#             for kle, value in dico_REN.items():
#                 stocker(f"{gen_path}Upsetplot_intersection/Sous_Corpus/{metadata_ocr[0]}_{metadata_ocr[1]}_{kle}.json" ,value, True)
# # ___________________________Par SOUS CORPUS____________________________


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


