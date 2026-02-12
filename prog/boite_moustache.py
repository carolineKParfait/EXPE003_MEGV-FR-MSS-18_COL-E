# Ce script permet la création des graphiques de l'évaluation de l'HTR (entre textes de REF et OCR) et de la NER il faut lire les commentaire pour adapter le programme au besoin
# Ce script a été lancé sous windows et Fedora (Linux) avec succès
# en ligne de commande sous windows avant, puis sélectionner le projet sous le disque X. Pour contrer la limitation des caractères dans les noms de chemin subst X: "C:\Users\Administrator\Documents\AVH2027_carolinekoudoroparfait"
import glob
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("TkAgg")  # ou "Qt5Agg" si tu as PyQt5 installé
import matplotlib.pyplot as plt
from renommage import *


def boxplot(data_tab, x_col ,y_col):
    # Initialize the figure with a logarithmic x axis
    f, ax = plt.subplots(figsize=(15, 15))
    ax.set_xscale("linear")
    # Plot the orbital period with horizontal boxes
    sns.boxplot(x=x_col, y=y_col, data=data_tab,
                whis=[0, 1], width=.6,
                palette="coolwarm")
    # Add in points to show each observation
    sns.stripplot(x=x_col, y=y_col, data=data_tab,
                  size=4, palette='dark:.3',
                  linewidth=0)
    # Tweak the visual presentation
    plt.tick_params(axis='both', labelsize=25)
    ax.xaxis.grid(True)

    # 👉 Ajout des légendes
    ax.set_xlabel(x_col, fontsize=25)
    ax.set_ylabel(y_col, fontsize=25)
    plt.xlim([0, x_col])

def chemin_stockage(sim_path) :
    sim_path.mkdir(parents=True, exist_ok=True)
    return sim_path

type_calcul=["sim2-3"]
calc=type_calcul[-1]
liste_cle=["cosinus","jaccard"]
size=[1]

corpora_data = ["DATA", "DATA-COL-E"]
corpus_data = corpora_data[1]
path_data =f"../{corpus_data}/anom_col-e-vrac2"

for cle in liste_cle:
    # ##____Pour les Textes_____________________
    # tableau = {}
    # liste_version_spacy = []
    # liste_config = []
    # liste_dist = []
    # liste_sous_corpus = []
    # liste_name_metric = []
    # liste_version_ren = []
    # ##____Pour les Textes_____________________
    for path_corpus in glob.glob(path_data):
        print("path_corpus",path_corpus)
        ##____Pour la NER_____________________
        tableau={}
        liste_version_spacy=[]
        liste_config=[]
        liste_dist=[]
        liste_sous_corpus=[]
        liste_name_metric=[]
        liste_version_ren=[]
        ##____Pour la NER_____________________

        # for path in glob.glob(f"{path_corpus}/*OCR/*/SIM/{calc}*.json"):##Texte
        for path in glob.glob(f"{path_corpus}/*OCR/*/NER*/SIM/{calc}*.json"):##NER
            p = Path(path)
            print("Path :", p)
            corpus = p.parts[1]
            print("Corpus :", corpus)
            sous_corpus = p.parts[2]
            print("Sous-corpus : ", sous_corpus)
            nom_fichier = p.parts[-1].split("_")[1]
            print("Nom du fichier :", nom_fichier)

#             # ##____Pour les Textes_____________________
#             # version = p.parts[-1]
#             # version = Path(version.split("_")[-1]).stem
#             # print("Version : ", version)
#             # ##____Pour les Textes_____________________

            ##____Pour la NER_____________________
            version = p.parts[-1]
            version=version.split("_")[-2]
            print("Version : ",version)
            vers_ren = p.parts[-1]
            vers_ren = Path(vers_ren.split("_")[-1]).stem
            print("Version de NER : ",vers_ren)
            ##____Pour la NER_____________________
            nommage_version = nommage(version)
            print("Nommage version : ", nommage_version)
            distance=lire_fichier(path)
            print("Distance : ", distance)



            # liste_distance=[]
            for key, res_dist in distance.items():
                print("Key : ",key)
                if key == cle:
                    for res in res_dist:
                        liste_name_metric.append(key)
                        # print("Liste des noms de métric : ", liste_name_metric)
                        # liste_config.append(nommage_version+" -- "+"REF")#Pour Textes
                        liste_config.append(nommage_version+" -- "+vers_ren)#Pour NER
                        liste_sous_corpus.append(sous_corpus)
                        liste_dist.append(res)
                        liste_version_ren.append(vers_ren)#Pour NER
#
        tableau["Corpus"]=liste_sous_corpus
        tableau["Configuration"]=liste_config
        tableau[f"Distance {cle}"]=liste_dist
        tableau["Metric"]=liste_name_metric
        tableau["REN"]=liste_version_ren ##Pour NER
        df_sim = pd.DataFrame(tableau)
        # print(data_tab)
#
        for x in size:
            sns.set_theme(style="ticks")
            # boxplot(df_sim,f"Distance {cle}","Corpus")##Pour Texte
            boxplot(df_sim, f"Distance {cle}", "Configuration")##Pour NER


        bm_path_txt = p.parent.parent.parent.parent.parent / "Boite_moustache" / nommage_version
        bm_path_ner = p.parent.parent.parent / "Boite_moustache" / nommage_version
        bm_path = chemin_stockage(bm_path_ner)
        # plt.show()

# ##____Pour les Textes_____________________
#     plt.savefig(f"{bm_path}/{calc}_global_{cle}.png", dpi=300, bbox_inches="tight")  ##Texte
# ##____Pour les Textes_____________________
#
# # ##____Pour la NER_____________________
        plt.savefig(f"{bm_path}/{calc}_{sous_corpus}_{version}_{cle}.png",dpi=300, bbox_inches="tight")##NER
# # ##____Pour la NER_____________________
# plt.close()
