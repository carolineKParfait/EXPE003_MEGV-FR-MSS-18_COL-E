# Ce script fait l'évaluation de l'HTR (entre textes de REF et OCR) et de la NER il faut lire les commentaire pour adapter le programme au besoin
# Ce script a été lancé sous windows avec succès/il devrait fonctionner pour distributions linux mais à tester
# en ligne de commande sous windows avant, puis sélectionner le projet sous le disque X. Pour contrer la limitation des caractères dans les noms de chemin subst X: "C:\Users\Administrator\Documents\AVH2027_carolinekoudoroparfait"

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

def lire_dico(fichier_json):
    liste_en = []
    for key, value in fichier_json.items():
        for k, v in value.items():
            if k == "text":
                liste_en.append(v)
    return " ".join(liste_en)

def traiter_corpus(reference_files,ocr_files, is_json=False):
    #  configNER et configNER_ocr pour la NER par pour Textes
    for reference_file in reference_files:
        print("Chemin du fichier de REF : ", reference_file)
        name_ref = get_model_name(reference_file)
        # print("Nom du fichier de REF base : ", name_ref)
        name_ref_file = name_ref.split(".")[0]
        # print("Nom du fichier de REF : ",name_ref_file)
        version = "REF"
        configNER = name_ref.split("_")[-1]
        print("Nom du fichier REF", name_ref_file, "|| Version :", version, "|| configNER :", configNER)
        texte_ref = lire_fichier(reference_file, is_json=is_json)
        # print("Texte du fichier de REF : ", texte_ref)
        # print("Longueur du texte en caractère : ", len(texte_ref))

        # Pour l'eval sur la REN
        if is_json == True:
            ner_res = lire_dico(texte_ref)
            # print(ner_res)

        if not texte_ref:
            print("→ Référence ignorée (vide)")
            continue

        for ocr_file in ocr_files:
            print("Chemin du fichier OCR : ", ocr_file)
            name_ocr = get_model_name(ocr_file)
            print("Nom du fichier OCR base : ",name_ocr)
            name_ocr_file = name_ocr.split("_")[0]
            # print("Nom du fichier OCR : ",name_ocr_file)
            model_name_ocr = name_ocr.split("_")[-1]## pour Textes
            # model_name_ocr = name_ocr.split("_")[-2].split(".")[0]## pour NER
            configNER_ocr = name_ocr.split("_")[-1]
            print("Nom du fichier OCR",name_ocr_file,"|| OCR model :", model_name_ocr,"|| configNER :",configNER_ocr)
            texte_ocr = lire_fichier(ocr_file, is_json=is_json)
            # print("Texte OCR :", texte_ocr)

            # Pour l'eval sur la REN
            if is_json == True:
                ner_res_ocr = lire_dico(texte_ocr)
                print(ner_res_ocr)

            if not texte_ocr:
                print("→ OCR ignoré (vide)")
                continue
        #
            sim_path = ocr_file.parent / "SIM"
            sim_path.mkdir(parents=True, exist_ok=True)

            if name_ref_file == name_ocr_file:## pour Textes
            # if name_ref_file == name_ocr_file and configNER == configNER_ocr:## pour NER
                print("La comparaison est OK....")
                distance_txt = get_distances(texte_ref, texte_ocr)## pour Textes
                # distance_txt = get_distances(ner_res, ner_res_ocr)## pour NER
                print("Distances :", distance_txt)
                print("____________________________________________________________")
                print("____________________________________________________________")
                clean_eval_scores_txt = evaluate_file(reference_file, ocr_file)
                clean_eval_scores_txt = {x: y for x, y in clean_eval_scores_txt.items() if "tag" not in x}

                new_scores_text = get_new_scores(texte_ref, texte_ocr)## pour Textes
                # new_scores_text = get_new_scores(str(ner_res), str(ner_res_ocr))## pour NER
                print("Nouveaux scores :", new_scores_text)

                new_scores_text["clean_eval"] = clean_eval_scores_txt
                for k, v in distance_txt.items():
                    new_scores_text[k] = v
                json_path = (sim_path / f"sim2-3_{name_ocr_file}_{model_name_ocr}.json").resolve() ## pour Textes
                # json_path = (sim_path / f"sim2-3_{name_ocr_file}_{model_name_ocr}_{configNER_ocr}.json").resolve() ## pour NER # absolu
                if json_path.is_file():  # Vérifie que c'est un vrai fichier
                    print("Already DONE : ", json_path)
                    continue

                print("Écriture JSON :", json_path)
                with open(json_path, "w", encoding="utf-8") as w:
                    json.dump(new_scores_text, w, indent=2)
            else:
                print("La comparaison n'est pas OK....")
                print("____________________________________________________________")
                print("____________________________________________________________")
                continue

# Vérifie que le chemin du dossier DATA est passé en argument
if len(sys.argv) < 2:
    print("Donner le chemin des dossiers auteurs en argument (généralement DATA/)")
    exit()

# Crée un dossier temporaire si nécessaire
os.makedirs("tmp", exist_ok=True)

# Chemin vers le dossier des sous-corpus
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

    # Recherche des fichiers références et OCR pour les textes
    reference_files = list(auteur.glob("*REF/*.txt"))
    ocr_paths = list(auteur.glob("*OCR/*/*.txt"))
    traiter_corpus(reference_files, ocr_paths, False)

    # # Recherche des fichiers références et OCR pour les sorties de REN
    # reference_ren_files = list(auteur.glob("*REF/NER*/*.json"))
    # ocr_ren_paths = list(auteur.glob("*OCR/*/NER*/*.json"))
    # traiter_corpus(reference_ren_files, ocr_ren_paths, True)

