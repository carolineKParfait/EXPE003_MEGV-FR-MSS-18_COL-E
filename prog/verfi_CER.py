import glob
from generic_tools import *
import pandas as pd

path_sim = "../DATA-COL-E/*/*_OCR/*/SIM/*.json"
liste_cer = []
liste_nom_fichier = []
tableau = {}
for file_sim in glob.glob(path_sim):
 print(file_sim)
 resultats = lire_fichier(file_sim, True)
 for cle, valeur in resultats.items():
  print(cle)
  if cle == "KL_res":
   for k, v in valeur.items():
    if k == "CER":
     print(k,v)
     liste_cer.append(v)
     liste_nom_fichier.append(file_sim.split("/")[-1])

   tableau["CER"] = liste_cer
   tableau["Nom fichier"] = liste_nom_fichier
   df_sim = pd.DataFrame(tableau)
   print(df_sim)

