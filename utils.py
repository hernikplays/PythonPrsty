from os import path,mkdir
from time import sleep

def load_text(path): # načte soubor s textem
    file = ""
    try:
        file = open(path)
    except:
        return ""
    current_text = file.readlines()
    text = []
    for l in current_text:
        text.append(l.replace('\n', '⤶'))
    
    file.close()
    return text

def delka_textu(text):
    delka = 0
    for x in text:
        delka+=len(x)
    return delka

def otevri_chyby(filename):
    filepath = f"./chyba_cache/{filename}.prst"
    if(not path.exists(filepath)):
        if(not path.exists("./chyba_cache") or not path.isdir("./chyba_cache")): mkdir("./chyba_cache")
        return ""
        
    file = open(filepath,"r")
    current_text = file.readlines()
    text = []
    for l in current_text:
        text.append(l.replace('\n', '⤶'))
    
    file.close()
    return "⤶".join(text)

def zapis_chybu(chybne_slovo,jmeno):
    chyby = otevri_chyby(jmeno)
    chyby = chybne_slovo.replace("⤶","") + " "+ chyby

    file = open(f"./chyba_cache/{jmeno}.prst","wb")
    file.write(chyby.encode("utf-8"))
    

def welcome():
    print("  _____       _   _                 ")
    sleep(0.1)
    print(" |  __ \     | | | |                ")
    sleep(0.1)
    print(" | |__) |   _| |_| |__   ___  _ __  ")
    sleep(0.1)
    print(" |  ___/ | | | __| '_ \ / _ \| '_ \ ")
    sleep(0.1)
    print(" | |   | |_| | |_| | | | (_) | | | |")
    sleep(0.1)
    print(" |_|___ \__, |\__|_| |_|\___/|_| |_|")
    sleep(0.1)
    print(" |  __ \ __/ |  | |                 ")
    sleep(0.1)
    print(" | |__) |___/___| |_ _   _          ")
    sleep(0.1)
    print(" |  ___/ '__/ __| __| | | |         ")
    sleep(0.1)
    print(" | |   | |  \__ \ |_| |_| |         ")
    sleep(0.1)
    print(" |_|   |_|  |___/\__|\__, |         ")
    sleep(0.1)
    print("                      __/ |         ")
    sleep(0.1)
    print("                     |___/          ")
    