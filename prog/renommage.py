import re
import json
def lire_fichier (chemin):
    with open(chemin) as json_data:
        texte =json.load(json_data)
    return texte



def nommage(version):

    if version == "fonduegdmegvv2":
        version = re.sub("fonduegdmegvv2", "FoNDUE-GD-MEGV_v2", version)

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