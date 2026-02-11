import os
import glob

# # Liste des fichiers à fusionner (mettez les chemins complets si nécessaires)
# fichiers_a_fusionner = ["fichier1.txt", "fichier2.txt", "fichier3.txt"]
#
# # Nom du fichier de sortie
# fichier_sortie = "fusion.txt"
# path_coprus = ("../DATA/*")
#
# for path in glob.glob(f"{path_coprus}/*/*"):
#     print(path)
# with open(fichier_sortie, "w", encoding="utf-8") as sortie:
#     for nom_fichier in fichiers_a_fusionner:
#         if os.path.exists(nom_fichier):
#             with open(nom_fichier, "r", encoding="utf-8") as f:
#                 contenu = f.read()
#                 sortie.write(contenu + "\n")  # ajoute un saut de ligne entre les fichiers
#         else:
#             print(f"Attention : {nom_fichier} n'existe pas et sera ignoré.")
#
# print(f"Fusion terminée ! Le fichier '{fichier_sortie}' contient maintenant tout le texte.")


path_corpus = "../DATA-COL-E_renom/*/*OCR/*/*"

for path in glob.glob(path_corpus):
    if 'SIM' in path:
        print(path)