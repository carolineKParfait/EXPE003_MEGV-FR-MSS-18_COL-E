from supervenn import supervenn
from matplotlib import pyplot as plt
import glob
import json
import numpy as np
import pandas as pd
from upsetplot import from_memberships
from matplotlib import pyplot as plt
from upsetplot import from_contents, UpSet, plot
def lire_json (chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data


def titre_auteur(chemin):
    nomfich= chemin.split("/")[-1]
    # nomfich= nomfich.split(".")[0]
    # nomfich= nomfich.split("_")
    # # nomfich= nomfich.upper()
    # nomfich= ("_").join([nomfich[0]])
    return nomfich


def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)

    return chemin



path_corpora = "../Upstplt-ELTeC/*Por_sp*.json"

liste_moteur=[]
a=4
for path in glob.glob(path_corpora):
    print("_____________",path)
    path_output ="_".join(path.split("_")[:3])
    print(path_output)
    dico_entite=lire_json(path)
    # print(dico_entite)
    for key, value in dico_entite.items():
        liste_moteur.append(key)


    dico_entite = {k: set(v)for k,v in dico_entite.items() if k ==liste_moteur[a] or k =="Ref"}
    print(dico_entite)
    # for k, v in dico_entite.items():
    #     print(k,set(v))

    test = from_contents(dico_entite)
    upset = UpSet(
        test,
        orientation='horizontal',
        sort_by='degree',
        # subset_size='count',
        # show_counts=True,
        totals_plot_elements=3,
        show_percentages=True
    )


    # upset.style_subsets(
    #     present=["sm", "lg"],
    #     absent=[
    #         "flair",
    #         "camenBert"
    #     ],
    #     edgecolor="yellow",
    #     facecolor="blue",
    # )
    fig = plt.figure()
    fig.legend(loc=7)
    plt.subplots_adjust(left=0.112, right=0.975, top=0.782, bottom=0.101, wspace=0.2, hspace=0.2)
    upset.plot(fig=fig)
    for text in fig.findobj(plt.Text):
        if "%" in text.get_text():
            text.set_fontsize(8)
    # plt.suptitle("Représentation de \n l'intersection des lexiques", fontsize=20)
    # fig.figsize = (10, 6)
    plt.axis([-1, 2.3, 0, 6000])
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.savefig(path_output+"_%s_upsetplot.png"%liste_moteur[a], dpi=300)
    plt.show()



