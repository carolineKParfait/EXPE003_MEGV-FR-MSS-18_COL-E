import re
import json
def lire_fichier (chemin):
    with open(chemin) as json_data:
        texte =json.load(json_data)
    return texte
# #_______________ARCHEOLOGIE DE SPACY _____________________________________________________
def archeo_nommage(version, vers_ren):
    ##Kraken
    ##Kraken fr
    if version=="Kraken-base.txt" or version=="Kraken-base" or version=="kraken" or version=="Kraken" :
        version=re.sub("Kraken-base.txt|Kraken-base|kraken|Kraken",f"Kraken -- {vers_ren}",version)
        # print("Version : ", version)

    if version=="kraken-jspll-pretrain.txt" or version=="kraken-jspll-pretrain":
        version=re.sub("kraken-jspll-pretrain.txt|kraken-jspll-pretrain",f"Kraken--jspl-fr -- {vers_ren}",version)
        # print("Version : ", version)

    if version=="kraken-jspll-ELTeC.txt" or version=="kraken-jspll-ELTeC" :
        version=re.sub("kraken-jspll-ELTeC.txt|kraken-jspll-ELTeC",f"Kraken--jspl-ELTeCfr -- {vers_ren}",version)
        # print("Version : ", version)

    if version == "kraken4.3.13.dev25":
        version = re.sub("kraken4.3.13.dev25", f"Kraken 4.3.13 -- {vers_ren}", version)
        # print("version : ", version)

    if version == "kraken4.3.13.dev25-jspll-pretrain":
        version = re.sub("kraken4.3.13.dev25-jspll-pretrain", f"Kraken 4.3.13--jspl-fr -- {vers_ren}", version)
        # print("version : ", version)

    if version == "kraken4.3.13.dev25-jspll-ELTeC":
        version = re.sub("kraken4.3.13.dev25-jspll-ELTeC", f"Kraken 4.3.13--jspl-ELTeCfr -- {vers_ren}", version)
        # print("version : ", version)

    if version == "lectaurep-kraken4.3.13.dev25":
        version = re.sub("lectaurep-kraken4.3.13.dev25", f"Kraken Lectp. 4.3.13 -- {vers_ren}", version)
        # print("version : ", version)

    if version == "lectaurep-kraken4.3.13.dev25-jspll-pretrain":
        version = re.sub("lectaurep-kraken4.3.13.dev25-jspll-pretrain", f"Kraken Lectp. 4.3.13--jspl-fr -- {vers_ren}", version)
        # print("version : ", version)

    if version == "lectaurep-kraken4.3.13.dev25-jspll-ELTeC":
        version = re.sub("lectaurep-kraken4.3.13.dev25-jspll-ELTeC", f"Kraken Lectp. 4.3.13--jspl-ELTeCfr -- {vers_ren}", version)
        # print("version : ", version)

    ##Kraken en

    if  version=="Kraken-jspll-ELTeC":
        version=re.sub("Kraken-jspll-ELTeC",f"Kraken--jspl-ELTeCen -- {vers_ren}",version)
        # print("Version : ", version)
    if  version=="Kraken-jspll-pretrain":
        version=re.sub("Kraken-jspll-pretrain",f"Kraken--jspl-en -- {vers_ren}",version)
        # print("Version : ", version)

    ##Kraken pt
    if  version=="Kraken-jspl-ELTeC":
        version=re.sub("Kraken-jspl-ELTeC",f"Kraken--jspl-ELTeCpt -- {vers_ren}",version)
        # print("Version : ", version)
##Tess
    ##Tess fr
    if version=="TesseractFra-PNG.txt" or version=="TesseractFra-PNG" or version=="TesseractFra-png":
        version=re.sub("TesseractFra-PNG.txt|TesseractFra-PNG|TesseractFra-png",f"Tess. fr -- {vers_ren}",version)
        # print("Version : ", version)

    if version=="TesseractFra-PNG-jspll-pretrain.txt" or version=="TesseractFra-PNG-jspll-pretrain":
            version=re.sub("TesseractFra-PNG-jspll-pretrain.txt|TesseractFra-PNG-jspll-pretrain",f"Tess. fr--jspl-fr -- {vers_ren}",version)
            # print("Version : ", version)

    if version=="TesseractFra-PNG-jspll-ELTeC.txt" or version=="TesseractFra-PNG-jspll-ELTeC":
        version=re.sub("TesseractFra-PNG-jspll-ELTeC.txt|TesseractFra-PNG-jspll-ELTeC",f"Tess. fr--jspl-ELTeCfr -- {vers_ren}",version)
        # print("Version : ", version)

    if version == "tesseract0.3.10":
        version = re.sub("tesseract0.3.10", f"Tess. fr 3.10 -- {vers_ren}", version)
        # print("version : ", version)

    if version == "tesseract0.3.10-jspll-pretrain":
        version = re.sub("tesseract0.3.10-jspll-pretrain", f"Tess. fr 3.10--jspl-fr -- {vers_ren}", version)
        # print("version : ", version)

    if version == "tesseract0.3.10-jspll-ELTeC":
        version = re.sub("tesseract0.3.10-jspll-ELTeC", f"Tess. fr 3.10--jspl-ELTeCfr -- {vers_ren}", version)
        # print("version : ", version)

    ##Tess en
    if version=="tesseract" or version=="Tesseract-PNG":
         version=re.sub("tesseract|Tesseract-PNG",f"Tess. -- {vers_ren}",version)###ATTENTION à LA LANGUE
         # print("Version : ", version)

    if  version=="tesseract-jspll-pretrain" or version =="Tesseract-PNG-jspll-pretrain" :
        version=re.sub("tesseract-jspll-pretrain|Tesseract-PNG-jspll-pretrain",f"Tess.--jspl-en -- {vers_ren}",version)
        # print("Version : ", version)

    if  version=="Tesseract-PNG-jspll-ELTeC":
        version=re.sub("Tesseract-PNG-jspll-ELTeC",f"Tess.--jspl-ELTeCen -- {vers_ren}",version)
        # print("Version : ", version)

    if version == "tesseract0.3.10":
        version = re.sub("tesseract0.3.10", f"Tess. fr 3.10 -- {vers_ren}", version)
        # print("version : ", version)

    ##Tess pt

    if version=="TesseractPor-PNG":
        version=re.sub("TesseractPor-PNG",f"Tess. pt -- {vers_ren}",version)
        # print("Version : ", version)

    if version =="TesseractPor-PNG-jspl-ELTeC":
        version=re.sub("TesseractPor-PNG-jspl-ELTeC",f"Tess. pt--jspl-ELTeCpt -- {vers_ren}",version)
        # print("Version : ", version)

    if version == "PP.txt" or version == "REF.txt" or version == "REF" :
        version = re.sub("PP.txt|REF.txt|REF", f"Ref. -- {vers_ren}", version)

    return version
#_______________ARCHEOLOGIE DE SPACY _____________________________________________________

def nommage(version):
    # if version == "Tesseract-ACCMAJ" or "Kraken-ACCMAJ":
    #     version = re.sub("Tesseract-ACCMAJ|Kraken-ACCMAJ", "Accord majoritaire (OCR)", version)
    #
    # if version == "Tesseract-GOLD" or "Kraken-GOLD":
    #     version = re.sub("Tesseract-GOLD|Kraken-GOLD", "GOLD (OCR)", version)
    #
    # if version == "REF-GOLD" :
    #     version = re.sub("REF-GOLD", "GOLD (Réf.)", version)
    #
    # if version == "REF-ACCMAJ" :
    #     version = re.sub("REF-ACCMAJ", "Accord majoritaire (Réf.)", version)

    if version == "PP" or version == "REF":
        version = re.sub("PP", "Ref.", version)
        # print("key : ", version)

    if version == "Ref" :
        version = re.sub("Ref", "ACCMAJ", version) ## POUR TAL−ENS2
        # version = re.sub("Ref", "GOLD", version)## POUR TAL−ENS2
    #     print("key : ", version)

    if version == "Kraken-base.txt" or version == "Kraken-base" or version == "Krakenbase" or version == "krakenbase" or version == "kraken" or version == "Kraken":
        version = re.sub("Kraken-base.txt|Kraken-base|Krakenbase|krakenbase|kraken|Kraken", f"Kraken", version)
        # print("Version : ", version)

    if version == "kraken-jspll-pretrain.txt" or version == "kraken-jspll-pretrain":
        version = re.sub("kraken-jspll-pretrain.txt|kraken-jspll-pretrain", "Kraken--jspl-fr", version)
        # print("Version : ", version)
    if version == "Kraken-jspll-pretrain":
        version = re.sub("Kraken-jspll-pretrain", "Kraken--jspl-en", version)
        # print("Version : ", version)

    if version == "kraken-jspll-ELTeC.txt" or version == "kraken-jspll-ELTeC":
        version = re.sub("kraken-jspll-ELTeC.txt|kraken-jspll-ELTeC", "Kraken--jspl-ELTeCfr", version)
        # print("Version : ", version)
    if version == "Kraken-jspll-ELTeC":
        version = re.sub("Kraken-jspll-ELTeC", "Kraken--jspl-ELTeCen", version)
        # print("Version : ", version)
    if version == "Kraken-jspl-ELTeC":
        version = re.sub("Kraken-jspl-ELTeC", "Kraken--jspl-ELTeCpt", version)
        # print("Version : ", version)

    if version == "TesseractFra-PNG.txt" or version == "TesseractFra-PNG" or version == "TesseractFra-png":
        version = re.sub("TesseractFra-PNG.txt|TesseractFra-PNG|TesseractFra-png", f"Tess. fr", version)
        # print("Version : ", version)

    if version == "tesseract" or version == "Tesseract-PNG":
        version = re.sub("tesseract|Tesseract-PNG", "Tess.", version)  ###ATTENTION à LA LANGUE
        # print("Version : ", version)

    if version == "TesseractPor-PNG":
        version = re.sub("TesseractPor-PNG", "Tess. pt", version)
        # print("Version : ", version)

    if version == "TesseractFra-PNG-jspll-pretrain.txt" or version == "TesseractFra-PNG-jspll-pretrain":
        version = re.sub("TesseractFra-PNG-jspll-pretrain.txt|TesseractFra-PNG-jspll-pretrain", "Tess. fr -- jspl-fr",
                         version)
        # print("Version : ", version)

    if version == "tesseract-jspll-pretrain" or version == "Tesseract-PNG-jspll-pretrain":
        version = re.sub("tesseract-jspll-pretrain|Tesseract-PNG-jspll-pretrain", "Tess. -- jspl-en", version)
        # print("Version : ", version)

    if version == "TesseractFra-PNG-jspll-ELTeC.txt" or version == "TesseractFra-PNG-jspll-ELTeC":
        version = re.sub("TesseractFra-PNG-jspll-ELTeC.txt|TesseractFra-PNG-jspll-ELTeC", "Tess. fr -- jspl-ELTeCfr",
                         version)
        # print("Version : ", version)
    if version == "Tesseract-PNG-jspll-ELTeC":
        version = re.sub("Tesseract-PNG-jspll-ELTeC", "Tess. -- jspl-ELTeCen", version)
        # print("Version : ", version)
    if version == "TesseractPor-PNG-jspl-ELTeC":
        version = re.sub("TesseractPor-PNG-jspl-ELTeC", "Tess. pt -- jspl-ELTeCpt", version)
        # print("Version : ", version)

    if version == "tesseract0.3.10" or version == "tesseract0":
        version = re.sub("tesseract0.3.10|tesseract0", "Tess. fr 3.10", version)
        # print("version : ", version)

    if version == "tesseract0.3.10-jspll-pretrain":
        version = re.sub("tesseract0.3.10-jspll-pretrain", "Tess. fr 3.10 -- jspl-fr", version)
        # print("version : ", version)

    if version == "tesseract0.3.10-jspll-ELTeC":
        version = re.sub("tesseract0.3.10-jspll-ELTeC", "Tess. fr 3.10 -- jspl-ELTeCfr", version)
        # print("version : ", version)

    if version == "kraken4.3.13.dev25" or version == "kraken4":
        version = re.sub("kraken4.3.13.dev25|kraken4", "Kraken 4.3.13", version)
        # print("version : ", version)

    if version == "kraken4.3.13.dev25-jspll-pretrain":
        version = re.sub("kraken4.3.13.dev25-jspll-pretrain", "Kraken 4.3.13 -- jspl-fr", version)
        # print("version : ", version)

    if version == "kraken4.3.13.dev25-jspll-ELTeC":
        version = re.sub("kraken4.3.13.dev25-jspll-ELTeC", "Kraken 4.3.13 -- jspl-ELTeCfr", version)
        # print("version : ", version)

    if version == "lectaurep-kraken4.3.13.dev25":
        version = re.sub("lectaurep-kraken4.3.13.dev25", "Kraken Lectp. 4.3.13", version)
        # print("version : ", version)

    if version == "lectaurep-kraken4.3.13.dev25-jspll-pretrain":
        version = re.sub("lectaurep-kraken4.3.13.dev25-jspll-pretrain", "Kraken Lectp. 4.3.13 -- jspl-fr", version)
        # print("version : ", version)

    if version == "lectaurep-kraken4.3.13.dev25-jspll-ELTeC":
        version = re.sub("lectaurep-kraken4.3.13.dev25-jspll-ELTeC", "Kraken Lectp. 4.3.13 -- jspl-ELTeCfr", version)
        # print("version : ", version)


        # new_dic[new_key] = value


    return version

def nommage_upset(key):
    if key == "Kraken-base.txt" or key == "kraken" or key == "Kraken":
        new_key = re.sub("Kraken-base.txt|kraken|Kraken", "Kraken", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "kraken-jspll-pretrain.txt" or key == "kraken-jspll-pretrain":
        new_key = re.sub("kraken-jspll-pretrain.txt|kraken-jspll-pretrain", "Kraken--jspl-fr", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "Kraken-jspll-pretrain":
        new_key = re.sub("Kraken-jspll-pretrain", "Kraken--jspl-en", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "kraken-jspll-ELTeC.txt" or key == "kraken-jspll-ELTeC":
        new_key = re.sub("kraken-jspll-ELTeC.txt|kraken-jspll-ELTeC", "Kraken--jspl-ELTeCfr", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "Kraken-jspll-ELTeC":
        new_key = re.sub("Kraken-jspll-ELTeC", "Kraken--jspl-ELTeCen", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "Kraken-jspl-ELTeC":
        new_key = re.sub("Kraken-jspl-ELTeC", "Kraken--jspl-ELTeCpt", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "TesseractFra-PNG.txt" or key == "TesseractFra-PNG" or key == "TesseractFra-png":
        new_key = re.sub("TesseractFra-PNG.txt|TesseractFra-PNG|TesseractFra-png", "Tess. fr", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "tesseract" or key == "Tesseract-PNG":
        new_key = re.sub("tesseract|Tesseract-PNG", "Tess.", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "TesseractPor-PNG":
        new_key = re.sub("TesseractPor-PNG", "Tess. pt", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "TesseractFra-PNG-jspll-pretrain.txt" or key == "TesseractFra-PNG-jspll-pretrain":
        new_key = re.sub("TesseractFra-PNG-jspll-pretrain.txt|TesseractFra-PNG-jspll-pretrain",
                         "Tess. fr -- jspl-fr", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "tesseract-jspll-pretrain" or key == "Tesseract-PNG-jspll-pretrain":
        new_key = re.sub("tesseract-jspll-pretrain|Tesseract-PNG-jspll-pretrain", "Tess. -- jspl-en", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "TesseractFra-PNG-jspll-ELTeC.txt" or key == "TesseractFra-PNG-jspll-ELTeC":
        new_key = re.sub("TesseractFra-PNG-jspll-ELTeC.txt|TesseractFra-PNG-jspll-ELTeC",
                         "Tess. fr -- jspl-ELTeCfr", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "Tesseract-PNG-jspll-ELTeC":
        new_key = re.sub("Tesseract-PNG-jspll-ELTeC", "Tess. -- jspl-ELTeCen", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "TesseractPor-PNG-jspl-ELTeC":
        new_key = re.sub("TesseractPor-PNG-jspl-ELTeC", "Tess. pt -- jspl-ELTeCpt", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "Ref":
        new_key = re.sub("Ref", "Ref.", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "tesseract0.3.10":
        new_key = re.sub("tesseract0.3.10", "Tess. fr 3.10", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "kraken4.3.13.dev25":
        new_key = re.sub("kraken4.3.13.dev25", "Kraken 4.3.13", key)
        print("key : ", new_key)
        # new_dic[new_key] = value

    if key == "lectaurep-kraken4.3.13.dev25":
        new_key = re.sub("lectaurep-kraken4.3.13.dev25", "Kraken Lectp. 4.3.13", key)
        print("key : ", new_key)
        # new_dic[new_key] = value
    return new_key