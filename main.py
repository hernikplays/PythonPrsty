from pynput import keyboard
from colorama import Fore,init,Back
import os
import utils

init()

# předdefinujeme proměnné
text = ""
toPsat = None # řádek, který má být právě psán
napsano = "" # to, co už uživatel napsal
thread = None # proměnná pro vlákno, abychom mohli input předčasně ukončit
listener = None # proměnná pro posluchač stisknutí kláves
radek = 0 # řádek, který zrovna píšeme
pismeno = 0 # písmeno, které právě máme psát

def main_menu():
    global text
    print(f"{Back.WHITE}{Fore.BLACK}Vyberte co chcete dělat:{Back.RESET}{Fore.RESET}")
    print("1 - načíst soubor s textem")
    if text != "":
        print("2 - Začít psat")
    else:
        print(f"{Fore.RED}2 - Začít psat{Fore.RESET}")
    choose = input()
    if(choose == "1"):
        path = input("Zadejte cestu k souboru s textem")
        text = utils.load_text(path)
        os.system("cls||clear")
        if(text == ""):
            print(f"{Fore.RED}Při otevírání souboru došlo k chybě{Fore.RESET}\n")
        main_menu()
    elif(choose == "2" and text == ""):
        print(f"{Fore.RED}Není načtený žádný text")
    elif(choose == "2"):
        pis()
        listener = keyboard.Listener(on_release=on_key_release)
        listener.start()
        input()


def pis():
    print(text[radek])
    print(napsano)
    

def on_key_release(key):
    global napsano,pismeno,radek,text
    p = text[radek][pismeno]
    try:
        if(p == key.char):
            napsano += key.char
        else:
            napsano += f"{Fore.RED}{key.char}{Fore.RESET}"
    except AttributeError:
        if(key == keyboard.Key.space):
            if(p == " "):
                napsano += " "
            else:
                napsano += f"{Fore.RED}_{Fore.RESET}"
        else: return
    pismeno+=1
    os.system("cls||clear")
    pis()
main_menu()
