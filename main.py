from time import time
from pynput import keyboard
from colorama import Fore,init,Back
import os
import utils
from sys import stdin

init()

# předdefinujeme proměnné
text = ""
toPsat = None # řádek, který má být právě psán
napsano = "" # to, co už uživatel napsal
thread = None # proměnná pro vlákno, abychom mohli input předčasně ukončit
listener = None # proměnná pro posluchač stisknutí kláves
radek = 0 # řádek, který zrovna píšeme
pismeno = 0 # písmeno, které právě máme psát
ctrl = False

start = 0 # začátek psaní
konec = 0 # konec psaní
chyby = 0 # chyby

def main_menu(): # funkce pro zobrazení hlavního menu
    global text,start,chyby
    print(f"{Back.WHITE}{Fore.BLACK}Vyberte co chcete dělat:{Back.RESET}{Fore.RESET}")
    print("1 - načíst soubor s textem")
    if text != "":
        print("2 - Začít psat")
    else:
        print(f"{Fore.RED}2 - Začít psat{Fore.RESET}")
    choose = input()
    if(choose == "1"):
        path = input("Zadejte cestu k souboru s textem\n")
        text = utils.load_text(path)
        os.system("cls||clear")
        if(text == ""):
            print(f"{Fore.RED}Při otevírání souboru došlo k chybě{Fore.RESET}\n")
        main_menu()
    elif(choose == "2" and text == ""):
        print(f"{Fore.RED}Není načtený žádný text")
    elif(choose == "2"):
        chyby = 0
        pis()
        start = time() # zaznamená čas, kdy začal uživatel psát
        listener = keyboard.Listener(on_release=on_key_release,on_press=on_key_press)
        listener.start() # spustí posluchač stisků
        stdin.read() # umožňuje, aby se program nezavřel


def pis(): # funkce jednoduše pro vypsání řádku a napsaného textu
    print(text[radek])
    print(napsano)
    

def on_key_press(key): # kontroloa pro control
    global ctrl
    if(key == keyboard.Key.ctrl_l):
        ctrl = True

def on_key_release(key): # funkce, která se spustí při puštění klávesy
    global napsano,pismeno,radek,text,chyby,ctrl
    p = text[radek][pismeno] # aktuálně psané písmeno
    try:
        if(key.vk == 90 and ctrl): # ctrl+z
            os.system("cls||clear")
            main_menu()
            return False
        elif(p == key.char): napsano += key.char # pokud se písmeno rovná znaku stisknuté klávesy, vložíme normálně
        else: 
            napsano += f"{Fore.RED}{key.char}{Fore.RESET}" # jinak vložíme červeně
            chyby+=1
    except AttributeError: # speciální klávesy jako je mezerník nevrací ".char" a vyhodí AttributeError
        if(key == keyboard.Key.space): # pokud je klávesa mezerník
            if(p == " "): napsano += " "
            else: 
                napsano += f"{Fore.RED}_{Fore.RESET}"
                chyby+=1
        elif(key == keyboard.Key.enter and pismeno != 0): # pokud je klávesa enter
            if(p == "⤶"): napsano += "\n"
            else: 
                napsano += f"{Fore.RED}⤶{Fore.RESET}\n"
                chyby+=1
        elif key == keyboard.Key.ctrl_l:
            ctrl = False
        else: return # jinak ignorovat
    if(pismeno+1 == len(text[radek]) and radek+1 != len(text)): # pokud jsme na konci řádku ale nejsme na konci textu
        radek+=1
        pismeno = 0
        napsano = ""
        os.system("cls||clear")
        pis()
    elif(pismeno+1 == len(text[radek]) and radek+1 == len(text)): # pokud jsme na konci řádku a konci textu
        hotovo()
    else: # jinak pokračujeme dál po písmenkách
        pismeno+=1
        os.system("cls||clear")
        pis()

def hotovo(): # finální vyhodnocení
    global konec
    konec = time()
    os.system("cls||clear")
    print("Úspěšně dopsáno")
    print()
    print(f"Chybné úhozy: {Fore.RED}{chyby}{Fore.RESET}")
    print()
    print(f"Průměrná rychlost: {Fore.CYAN}{(utils.delka_textu(text)/(konec-start))*60}{Fore.RESET} úhozů za minutu")
    print(f"\nStiskni {Fore.GREEN}Ctrl+Z{Fore.RESET} pro navrácení do menu")

utils.welcome()
main_menu()
