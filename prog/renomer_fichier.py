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
    parties = nom.rsplit("_", 1)
    if len(parties) == 2:
        avant, dernier = parties
        nouveau_nom = avant.replace("_", "-") + "_" + dernier
    else:
        nouveau_nom = nom  # Aucun "_" trouvé

    nouveau_nom_complet = nouveau_nom + extension
    nouveau_chemin = os.path.join(dossier, nouveau_nom_complet)

    # Renommer le fichier
    os.rename(chemin_fichier, nouveau_chemin)

    return nouveau_chemin


# Exemple d'utilisation

path_ref = "../DATA/an_corresp-prov-roch/*REF/*.txt"
path_ocr = "../DATA/an_corresp-prov-roch/*OCR/*/*.txt"

for path in glob.glob(path_ocr):
    print(path)
    ancien_fichier = path
    nouveau_fichier = renommer_fichier(ancien_fichier)

    print("Fichier renommé en :", nouveau_fichier)






