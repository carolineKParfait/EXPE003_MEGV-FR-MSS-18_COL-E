import glob
import pandas as pd
from upsetplot import from_memberships
from matplotlib import pyplot as plt
from upsetplot import from_contents, UpSet
import re
import os
from generic_tools import *
from collections import Counter
from upsetplot import UpSet
from upsetplot import plot

def chemin_stockage(path) :
    path.mkdir(parents=True, exist_ok=True)
    return path

# ##___________________GLOBAL_________________________________
# path_corpora = "../DATA-COL-E/Upsetplot_intersection/GLOBAL"
# ##___________________GLOBAL_________________________________
##___________________PAR SOUS-CORPUS_________________________
path_corpora = "../DATA-COL-E/Upsetplot_intersection/Sous_Corpus"
##___________________PAR SOUS-CORPUS_________________________________

liste_GT = ["REF"]
GT = liste_GT[0]
OCR =  "FoNDUE-GD-MEGV_v2"
size = [2000,3000]
liste_moteur = []

for path in glob.glob(f"{path_corpora}/*.json"):

    print(path)
    p = Path(path)

    dico_ups = lire_fichier(path, True)
    print(dico_ups)
    print("Clés",dico_ups.keys())

    # dico_entite = {k: set(v) for k, v in sorted(new_dic.items()) if k == liste_moteur[a] or k == GT}
    dico_entite = {k: set(v) for k, v in sorted(dico_ups.items())}
    test = from_contents(dico_entite)
    upset = UpSet(
        test,
        facecolor="silver",
        orientation='horizontal',
        sort_by='degree',
        # subset_size='count',
        # show_counts=True,
        totals_plot_elements=3,
        show_percentages=True
    )
    upset.style_subsets(
        present=GT,
        # label="Réf.",
        # absent=[
        #     "flair",
        #     "camenBert"
        # ],
        edgecolor="firebrick",
        # facecolor="dimgray",
        # hatch="xx"
    )
    upset.style_subsets(
        present= OCR,
        # label=liste_moteur[a],
        # absent=[
        #     "flair",
        #     "camenBert"
        # ],
        # edgecolor="royalblue",
        facecolor="steelblue",

    )

    for x in size:

        chemin_sortie = chemin_stockage(p.parent / "PNG")
        print("Chemin du dossier PNG : ", chemin_sortie)
        sortie = "/".join(p.parts[0:-1]) + "/PNG/" + Path(p.parts[-1]).stem + f"-{x}.png"
        print("Chemin du fichier de sortie : ", sortie)


        if os.path.exists(sortie) == False:
            fig = plt.figure()
            fig.legend(loc=7)
            plt.subplots_adjust(left=0.112, right=0.975, top=0.782, bottom=0.101, wspace=0.2, hspace=0.2)
            print("test.head() : ",test.head())
            print("test.index : ", test.index)
            print("upset.intersections : ", upset.intersections)
            upset.plot(fig=fig)
            for text in fig.findobj(plt.Text):
                if "%" in text.get_text():
                    text.set_fontsize(8)
            # plt.suptitle("Représentation de \n l'intersection des lexiques", fontsize=20)
            # fig.figsize = (10, 6)
            # plt.yscale('log', base=10)

            plt.axis([-1.0, 2.3, 0.0, x])
            plt.xticks(fontsize=8)
            plt.yticks(fontsize=8)
            plt.savefig(f"{sortie}", dpi=300)
            # plt.show()
            plt.close
