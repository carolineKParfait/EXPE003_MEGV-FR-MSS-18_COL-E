import glob
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("TkAgg")  # ou "Qt5Agg" si tu as PyQt5 installé
import matplotlib.pyplot as plt
from renommage import *
from pathlib import Path

def boxplot(xx,yy):
    # Plot the orbital period with horizontal boxes
    sns.boxplot(x=xx, y=yy, data=data_tab,
                whis=[0, 1], width=.6,
                palette="coolwarm")

    # Add in points to show each observation
    sns.stripplot(x=f"Distance {cle}", y="Auteur", data=data_tab,
                  size=4, palette='dark:.3',
                  linewidth=0)

# calcul=["sim2-3","word", "sim2-3-GOLD","sim2-3-ACCMAJ"]
calcul=["sim2-3"]
calc=calcul[-1]
liste_cle=["cosinus","jaccard"]
size=[1]
path_data =f"../DATA/*"##
for cle in liste_cle:
    # ##____Pour les Textes_____________________
    # tableau = {}
    # liste_version_spacy = []
    # liste_config = []
    # liste_dist = []
    # liste_auteur = []
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
        liste_auteur=[]
        liste_name_metric=[]
        liste_version_ren=[]
        ##____Pour la NER_____________________

        # for path in glob.glob(f"{path_corpus}/*OCR/*/SIM/{calc}*.json"):##Texte
        for path in glob.glob(f"{path_corpus}/*OCR/*/NER*/SIM/{calc}*.json"):##NER
            p = Path(path)
            print("Path :", p)
            corpus = p.parts[1]
            print("Corpus :", corpus)
            autor = p.parts[2]
            print("Auteur : ",autor)
            nom_fichier = p.parts[-1].split("_")[1]
            print("Nom du fichier :", nom_fichier)

            # ##____Pour les Textes_____________________
            # version = p.parts[-1]
            # version = Path(version.split("_")[-1]).stem
            # print("Version : ", version)
            # ##____Pour les Textes_____________________

            ##____Pour la NER_____________________
            version = p.parts[-1]
            version=version.split("_")[-2]
            print("Version : ",version)
            vers_ren = p.parts[-1]
            vers_ren = vers_ren.split("_")[-1]
            print("Version de NER : ",vers_ren)
            ##____Pour la NER_____________________

            distance=lire_fichier(path)
            print("Distance : ", distance)

            nommage_version = nommage(version)
            print("Nommage version : ", nommage_version)

            # liste_distance=[]
            for key, res_dist in distance.items():
                print("Key : ",key)
                if key == cle:
                    for res in res_dist:
                        liste_name_metric.append(key)
                        # liste_config.append(nommage_version+" -- "+"REF")#Pour Textes
                        liste_config.append(nommage_version+" -- "+vers_ren)#Pour NER
                        liste_auteur.append(autor)
                        liste_dist.append(res)
                        liste_version_ren.append(vers_ren)#Pour NER

        sim_path = p.parent.parent.parent / "Boite_moustache" / nommage_version
        sim_path.mkdir(parents=True, exist_ok=True)
        print(sim_path)
#
        tableau["Auteur"]=liste_auteur
        tableau["Configuration"]=liste_config
        tableau[f"Distance {cle}"]=liste_dist
        tableau["Metric"]=liste_name_metric
        tableau["REN"]=liste_version_ren ##Pour NER
        data_tab = pd.DataFrame(tableau)
        print(data_tab)
#
        for x in size:
            sns.set_theme(style="ticks")

            # Initialize the figure with a logarithmic x axis

            f, ax = plt.subplots(figsize=(15, 15))
            ax.set_xscale("linear")
            # boxplot(tableau[f"Distance {cle}"],tableau["Auteur"])##Pour Texte
            boxplot(tableau[f"Distance {cle}"], tableau["Configuration"])##Pour NER


            # Tweak the visual presentation
            plt.tick_params(axis='both', labelsize=25)
            ax.xaxis.grid(True)
            ax.set(ylabel="")
            plt.xlim([0, x])
            # plt.show()

##____Pour les Textes_____________________
    # plt.savefig(f"../DATA-COL-E/{calc}_global_{cle}.png", dpi=300, bbox_inches="tight")  ##Texte
##____Pour les Textes_____________________

# ##____Pour la NER_____________________
            plt.savefig(f"{sim_path}/{calc}_{autor}_{version}_{cle}.png",dpi=300, bbox_inches="tight")##NER
# ##____Pour la NER_____________________
plt.close()
