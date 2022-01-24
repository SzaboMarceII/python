#2 - Írjunk programot amely megkérdezi a felhasználó nevét majd üdvözlő szöveggel üdvözli. 
#Egyes logikai egészeket alkotó műveleteket függvényekkel oldjuk meg.
import time
import os
from nev import *

def udvozles(nev:str) -> None:
    print(f"Üdvözlöm {nev}!")


felhasznalo:str=nevBekeres()
udvozles(felhasznalo)
            