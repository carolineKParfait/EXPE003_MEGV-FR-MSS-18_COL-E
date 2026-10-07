## Normaliser les noms de fichiers HTR et REF pour anom

import glob
import os


def renommer_fichier(chemin_fichier):
    dossier, nom_fichier = os.path.split(chemin_fichier)

    # Séparer nom et extension
    nom, extension = os.path.splitext(nom_fichier)
    #Pour REF
    # nouveau_nom = nom.replace("_", "-")

    # Pour OCR
    # Remplacer tous les "_" sauf le dernier
    # parties = nom.rsplit("_", 1)
    # if len(parties) == 2:
    #     avant, dernier = parties
        # # # ______________Fichiers NER
        # nouveau_nom = avant.replace("_", "-") + "-" + dernier
        # # ______________Fichiers SIM global
        # nouveau_nom = avant.replace("_", "-") + "-" + dernier
        # # ________Fichiers SIM Par catégories __________________
        # nouveau_nom = avant.replace("_", "-") + "_" + dernier

    # else:
    #     nouveau_nom = nom  # Aucun "_" trouvé

    # nouveau_nom_complet = nouveau_nom + extension
    # nouveau_chemin = os.path.join(dossier, nouveau_nom_complet)
    nouveau_chemin = p.name.replace(
        "-Moderncamembert-4entities",
        "_Moderncamembert-4entities"
    )

    # Renommer le fichier
    # os.rename(chemin_fichier, nouveau_chemin)

    return nouveau_chemin


# Exemple d'utilisation

# ________Fichiers  __________________
path_ref = "../DATA-COL-E/*/*REF/NER-Moderncamembert_4entities/*_4entities.json"
path_ocr = "../DATA-COL-E/an_corresp-fougeu-conflans/*OCR/*/NER-Moderncamembert_4entities/*_4entities.json"

# # ______________Fichiers SIM global
# path_ref = "../DATAan_corresp-fougeu-conflans/*REF/NER-Moderncamembert_4entities/SIM/*_4entities.json"
# path_ocr = "../DATA/an_corresp-fougeu-conflans/*OCR/*/NER-Moderncamembert_4entities/SIM/*_4entities.json"

# # ________Fichiers SIM Par catégories __________________
# path_ref = "../DATAan_corresp-fougeu-conflans/*REF/NER-Moderncamembert_4entities/SIM/*_4entities_*.json"
# path_ocr = "../DATA/an_corresp-fougeu-conflans/*OCR/*/NER-Moderncamembert_4entities/SIM/*_4entities_*.json"

for path in glob.glob(path_ref):
    print("PATH : ",path)
    ancien_fichier = path
    nouveau_fichier = renommer_fichier(ancien_fichier)

    print("Fichier renommé en :", nouveau_fichier)






