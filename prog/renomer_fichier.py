

import glob
import os

def renamme(anc_nom, new_name):

    name_change = os.rename(anc_nom, new_name)
    return name_change


# paths = ["../DATA-COL-E/*/*REF" , "../DATA-COL-E/*/*OCR/"]
paths = "../DATA-COL-E/"
# for subcorpus in glob.glob(corpus_orig+"/Mémoi*/*"):
#     print(subcorpus)
for subcorpus in glob.glob(paths + "*/*REF"): ## */ pour OCR
    # print(subcorpus)
    for subsubcorpus in glob.glob(subcorpus + "/*/"):
        print(subsubcorpus)
    print("___________________________________\n")
    # for subsubcorpus in glob.glob(subcorpus + "NER-Moderncamembert-4entities/*.json"):
    #     print("Chemin d'entrée : ",subsubcorpus)

        # decoup_pathname = subsubcorpus.split("/")
        # # print("Découpage du chemin originel :",decoup_pathname)
        #
        # # correction_dossier = decoup_pathname[-1]
        # # nouveau_nom = correction_dossier.replace("_", "-")
        # # print("Correction du dossier originel :",nouveau_nom)
        #
        # # path_name = "/".join(decoup_pathname[:-1])+"/"+nouveau_nom ## Adapter l'index de la liste selon le chemin d'entrée
        # # print("Nom du chemin de sortie ", path_name)
        #
        # path_name = "/".join(decoup_pathname[:-1])  ## Adapter l'index de la liste selon le chemin d'entrée
        # # print("Nom du chemin de sortie ", path_name)
        #
        # file_name = decoup_pathname[-1].split("_")
        # # print("Liste du nom complet : ",file_name)
        # correction = "_".join(file_name[0:1])+"_"+"-".join(file_name[-2:])
        # # print("Correction : ",correction)
        # #
        # complet_name = path_name + "/" + correction
        # print("Chemin complet : ", complet_name)
        # # # print(complet_name)

## A décommanter à la fin lorsqu'on est certain du chemin en vérifiant le print de complet_name
        # renamme(subsubcorpus,complet_name)






