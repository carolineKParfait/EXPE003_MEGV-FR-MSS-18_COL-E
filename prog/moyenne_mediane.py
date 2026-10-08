#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:44:43 2024

@author: ceres
"""

import glob
import os
import json
import numpy as np



def lire_fichier_json(chemin):
    with open(chemin) as json_data: 
        texte = json.load(json_data)
    return texte


def moyenne(liste_res):
    somme = sum(liste_res)
    moyenne = somme/len(liste_res)
    return moyenne


def mediane(liste_resm):
    a = np.array(liste_resm)
    median_value = np.percentile(a, 50)
    return median_value


def stocker_json(chemin, contenu):
    with open(chemin, "w", encoding="utf-8") as w:
        w.write(json.dumps(contenu, indent=2, ensure_ascii=False))
    return


path_file = f"../DATA-COL-E/*/*OCR/*"
types_res = ["CER","cosinus"]
type_res = types_res[-1]

for path in glob.glob(path_file):
    # print("Chemin dossier d'entrée : ",path)

    ##______ Définir chemin d'entrée et chemin de sortie pour le fichier de résultats
    dec_pathname = path.split("/")
    # print("Découpe du chemin d'entrée : ", dec_filename)
    path_resultats = "/".join(dec_pathname[:]) + f"/Synthese-CER-Cosinus/"
    # print("Chemin du dossier de stockage des résultats", path_resultats)
# ______ Création du dossier de sortie
    os.makedirs(path_resultats, exist_ok=True)

    file_output = path_resultats + f"{type_res}_" + dec_pathname[-1]
    # print("Chemin du fichier de sortie : ", file_output)


#______ Définir Nom du moteur OCR
    moteur_ocr = dec_pathname[-1].split("_")[2]
    # print("Nom du Moteur OCR : ",moteur_ocr)


    dico_res = {}
    # for file in glob.glob(f"%s/SIM/*.json"%path): ##REF
    for file in glob.glob(f"{path}/NER-*/SIM/*.json"):  ##NER /NER-*/SIM/*
        print("Chemin du fichier d'entrée : ", file)
        dec_filename = file.split("/")
        print("Découpe du chemin fichier d'entrée : ", dec_filename)
        filename = dec_filename[-1]
        print("Nom chemin fichier d'entrée : ", filename)
#______ Définir Nom du système de REN

        ner_model =filename.split("_")[3]
        print("Nom du model de NER : ", ner_model)

##______ Vérification longueur nom du fichier if == 4 ner.json if == 5 _CATegorie.json
        long_filename = len(filename.split("_"))
        # print("Longueur nom du fichier",long_filename)

        if long_filename == 4 :
            print(long_filename, "-- Nom du fichier : ",filename)

            clef = moteur_ocr + "_" + ner_model
            data = lire_fichier_json(file)
            # print(data)
            if type_res == "cosinus":
                for key, value_dic in data.items():
                    # print(key,value_dic)
                    ## Pour récupérer le Cosinus
                    if key == type_res:
                        print(value_dic)
                        if clef in dico_res:
                            liste_CER = dico_res[clef]
                            liste_CER.append(value_dic[0])
                            dico_res[clef] = liste_CER
                        else:
                            dico_res[clef] = [value_dic[0]]
            # Pour récupérer le CER
                else :
                    if key == "KL_res":
                        # print(value_dic)
                        for k, v in value_dic.items():
                            if k == type_res:
                                if clef in dico_res:
                                    liste_CER = dico_res[clef]
                                    liste_CER.append(v)
                                    dico_res[clef] = liste_CER
                                else:
                                    dico_res[clef] = [v]

    print("DICO--RES ***** ", dico_res)


    dico_mediane={}
    for cle, valeur in dico_res.items():
        dico_mediane[cle]= {}
        dico_mediane[cle]["mediane"] = mediane(valeur)
        dico_mediane[cle]["moyenne"] = moyenne(valeur)

    print("DICO--Médiane ***** ",dico_mediane)
    stocker_json(f"{file_output}_dico-resultats.json", dico_res)
    stocker_json(f"{file_output}_moyenne-mediane.json", dico_mediane)

# Ecrire chemin de stockage plus facile


