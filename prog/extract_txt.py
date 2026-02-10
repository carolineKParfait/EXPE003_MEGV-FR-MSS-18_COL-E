import glob
import re
import os

def xml_strings_to_txt(xml_file, output_folder):
    # Création du dossier si nécessaire
    os.makedirs(output_folder, exist_ok=True)

    # Lire le fichier XML
    with open(xml_file, "r", encoding="utf-8") as f:
        data = f.read()

    # Extraire tous les CONTENT="..."
    pattern = r'<String[^>]*CONTENT="(.*?)"'
    contents = re.findall(pattern, data)

    # Récupérer tous les mots de tous les contenus
    all_words = []
    for content in contents:
        words = content.split()  # séparer en mots
        all_words.extend(words)

    # Nom de sortie basé sur le nom du fichier d'entrée
    base_name = os.path.splitext(os.path.basename(xml_file))[0]
    output_file = os.path.join(output_folder, f"{base_name}.txt")

    # Écriture dans un seul fichier texte
    # with open(output_file, "w", encoding="utf-8") as out:
    #     for line in contents:
    #         out.write(line + "\n")

    # Écriture dans un seul fichier texte, mots alignés sur une seule ligne
    with open(output_file, "w", encoding="utf-8") as out:
        out.write(" ".join(all_words))  # tous les mots séparés par des espaces

# Utilisation :
corpus = "../data_ocr/*"
for path in glob.glob(corpus):
    # print(path)
    for file in glob.glob(f"{path}/*.xml"):
        print(f"Traitement de : {file}")
        xml_strings_to_txt(file, path)
