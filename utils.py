from colorama import Fore
def load_text(path): # načte soubor s textem
    file = ""
    try:
        file = open(path)
    except:
        return ""
    current_text = file.readlines()
    file.close()
    return current_text