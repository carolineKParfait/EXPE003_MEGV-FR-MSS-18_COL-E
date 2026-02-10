from generic_tools import *

import re
import json
import sys
import os
from pathlib import Path

def create_str_ner(json_path, str_path):
    """
    Transforme la liste d'entités en une string
    les mots des entités multi-mots sont concaténés
    """
    with open(json_path, encoding="utf-8") as f:
        liste = json.load(f)
    # Corrige le warning avec raw string pour \s
    liste = [re.sub(r"\s", "", x) for x in liste]
    with open(str_path, "w", encoding="utf-8") as w:
        w.write(" ".join(liste))

def get_model_name(chemin):
    chemin = Path(chemin)
    model_name = chemin.stem  # nom du fichier sans extension
    return model_name

# Vérifie que le chemin du dossier DATA est passé en argument
if len(sys.argv) < 2:
    print("Donner le chemin des dossiers auteurs en argument (généralement DATA/)")
    exit()

# Crée un dossier temporaire si nécessaire
os.makedirs("tmp", exist_ok=True)

# Chemin vers le dossier des auteurs
path_auteurs = Path(sys.argv[1])
print("Chemin auteurs :", path_auteurs)

if not path_auteurs.exists() or not path_auteurs.is_dir():
    print("Problème: dossier non trouvé :", path_auteurs)
    exit()

# Liste des sous-dossiers (auteurs)
liste_dossiers_auteurs = [d for d in path_auteurs.iterdir() if d.is_dir()]
if len(liste_dossiers_auteurs) == 0:
    print("Problème: pas de sous-dossier trouvés dans", path_auteurs)
    exit()

# Parcours des dossiers auteurs
for auteur in liste_dossiers_auteurs:
    print("-" * 20)
    print("Auteur :", auteur.name)

    # Recherche des fichiers références et OCR
    reference_files = list(auteur.glob("*REF/*.txt"))
    ocr_paths = list(auteur.glob("*OCR/*/*.txt"))

    for reference_file in reference_files:
        model_name_ref = get_model_name(reference_file)
        print("Reference model :", model_name_ref)
        texte_ref = lire_fichier(reference_file)
        print("Texte ref :", texte_ref)
        if not texte_ref:
            print("→ Référence ignorée (vide)")
            continue

        for ocr_path in ocr_paths:
            model_name_ocr = get_model_name(ocr_path)
            configuration = ocr_path.name
            print("OCR model :", model_name_ocr, "Configuration :", configuration)

            sim_path = ocr_path.parent / "SIM"
            sim_path.mkdir(parents=True, exist_ok=True)

            texte_ocr = lire_fichier(ocr_path)
            print("____________________________________________________________")
            print("____________________________________________________________")
            print("____________________________________________________________")
            print("Texte ref (30 premiers caractères) :", repr(texte_ref[:30]))
            print("Texte OCR (30 premiers caractères) :", repr(texte_ocr[:30]))
            print("Longueurs :", len(texte_ref), len(texte_ocr))

            print("____________________________________________________________")
            print("____________________________________________________________")
            print("____________________________________________________________")
            if not texte_ocr:
                print("→ OCR ignoré (vide)")
                continue

            distance_txt = get_distances(texte_ref, texte_ocr)
            print("Distances :", distance_txt)

            clean_eval_scores_txt = evaluate_file(reference_file, ocr_path)
            clean_eval_scores_txt = {x: y for x, y in clean_eval_scores_txt.items() if "tag" not in x}

            new_scores_text = get_new_scores(texte_ref, texte_ocr)
            print("Nouveaux scores :", new_scores_text)

            json_path = sim_path / f"sim2-3_{configuration}"
            new_scores_text["clean_eval"] = clean_eval_scores_txt
            for k, v in distance_txt.items():
                new_scores_text[k] = v

            print("Écriture JSON :", json_path)
            with open(json_path, "w", encoding="utf-8") as w:
                json.dump(new_scores_text, w, indent=2)