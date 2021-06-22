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
    