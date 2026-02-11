import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from renommage import *
from pathlib import Path

# calcul=["sim2-3","word", "sim2-3-GOLD","sim2-3-ACCMAJ"]
calcul=["sim2-3"]
calc=calcul[-1]

path_data =f"../DATA/*"##
for path_corpus in glob.glob(path_data):
    print("path_corpus",path_corpus)
    tableau={}
    liste_version_spacy=[]
    liste_config=[]
    liste_dist=[]
    liste_auteur=[]
    liste_name_metric=[]
    liste_version_ren=[]

    for path in glob.glob(f"{path_corpus}/*OCR/*/NER*/SIM/{calc}*.json"):
        p = Path(path)
        print("Path :", p)
        corpus = p.parts[1]
        print("Corpus :", corpus)
        # autor=path.split("/")[1]##A adapter selon ARCHEO NER PAR_AUTEUR
        autor = p.parts[2]
        # autor=autor.split("_")[0]
        print("Auteur : ",autor)
        version = p.parts[-1]
        version=version.split("_")[-2]
        print("Version : ",version)
        vers_ren = p.parts[-1]
        vers_ren = vers_ren.split("_")[-1]
        print("Version de NER : ",vers_ren)
        distance=lire_fichier(path)
        print("Distance : ", distance)

        nommage_version = nommage(version)
        print("Nommage version : ", nommage_version)

        # liste_distance=[]
        for key, res_dist in distance.items():
            print("Key : ",key)
            if key == "cosinus" or key == "jaccard":
                for res in res_dist:
                    liste_name_metric.append(key)
                    liste_config.append(nommage_version+" -- "+vers_ren)#+"--"+paire)
                    liste_auteur.append(autor)
                    liste_dist.append(res)
                    liste_version_ren.append(vers_ren)


    tableau["Auteur"]=liste_auteur
    tableau["Configuration"]=liste_config
    tableau[f"Distance"]=liste_dist
    tableau["Metric"]=liste_name_metric
    tableau["REN"]=liste_version_ren ## Commenter pour OCR
    data_tab = pd.DataFrame(tableau)
    # data_tab=data_tab.sort_values(by = ['Configuration',"Metric","ArcheoREN"])
    print(data_tab)


    ## _____________NER graph 1 Modèle___________________________
    p=sns.relplot(data=data_tab, x="Configuration", y="Distance", hue="Metric", style="Metric", palette="autumn",s=800, height=8.7, aspect=11.7/8.27)
    sns.move_legend(p, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False,)
    ## _____________NER graph 1 Modèle___________________________
#
#    # _____________NER graph global Multi Modèles___________________________
#     p=sns.relplot(data=data_tab1, x="Configuration", y="Distance", hue="Metric", style="REN", palette="autumn",s=550,  height=8.7, aspect=11.7/8.27)
#    #  p=sns.relplot(data=data_tab1, x="REN", y="Distance", hue="Metric", style="REN", palette="autumn",s=550,  height=8.7, aspect=11.7/8.27)
#     sns.move_legend(p, "center right", bbox_to_anchor=(1, 1), ncol=1, title=None, frameon=False,)
#     # _____________NER graph global Multi Modèles___________________________
#
#     plt.tick_params(axis = 'both',grid_color='w', labelsize = 25)
#     plt.xticks(rotation=90)
#     plt.ylim([-0.1,1])
#     plt.xlim([-1,x])
#     plt.xlabel("Configurations",labelpad=40,loc="left")
#     plt.ylabel("Distances",labelpad=40)
#
#
# # # ####___________________PAR_AUTEUR________________________________________
    plt.savefig(f"../Boite-a_moustache/OCR/{corpus}/{autor}_{corpus}_{calc}.png",dpi=300, bbox_inches="tight")##Texte
#     plt.savefig(f"../Boite-a_moustache/PAR_AUTEUR/{corpus}/{autor}_{corpus}_{r}-{calc}.png",dpi=300, bbox_inches="tight")##NER
#     plt.close()
# # # ####___________________PAR_AUTEUR________________________________________