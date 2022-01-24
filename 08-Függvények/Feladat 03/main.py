#3 - Írjunk programot amely megkérdezi a felhasználó nevét és születési év, majd kiírja : ”Atila ön az idén 43 éves.”
#Egyes logikai egészeket alkotó műveleteket függvényekkel oldjuk meg

import datetime
import time
import os
felhasználoNev:str=None
szuletesiEv:int=None
kor:int=None


#nev bekérése
def nevBeolvasasa() -> int:
    eredmeny:str=None
    while(eredmeny==None):
        data:str=input("Kérem a nevét: ")
        if(len(data)>3):
            eredmeny=data
            return eredmeny
        else:
            print("Túl rövid nevet adott meg!")
        time.sleep(3)
        os.system("cls")
#születési év
def szuletesiEvBekerese()->int:
    eredmeny:int=None
    ma:datetime=datetime.datetime.now() #a mai datumot adja vissza
    jelenlegiEv:int=int(ma.strftime("%Y")) #visszaadha a jelenlegi évet dátumból

    while(eredmeny==None):
        data:str=input("Kérem adjon meg egy születési évet: ")
        if(data.isnumeric()):
            eredmeny=int(data)

            if(eredmeny>=jelenlegiEv):
                eredmeny=None
                print("A születési éve nem lehet nagyobb mint a jelenlegi év!")
                time.sleep(3)
                os.system("cls")
            else:
                return eredmeny
        
        else:
            print("Nem megfelelő születési évet adott meg!")
            time.sleep(3)
            os.system("cls")

#életkor kiszámitás
def eletkorKiszamitasa(ev:int)->int:
    ma:datetime=datetime.datetime.now()
    jelenlegiEv:int=int(ma.strftime("%Y"))

    return jelenlegiEv-ev
#kiiratás

def kiiratás(nev:str, ev:int)->None:
    print(f"{nev} ön az idén {ev} éves.")


#főprogram
felhasználoNev=nevBeolvasasa()
szuletesiEv=szuletesiEvBekerese()
kor=eletkorKiszamitasa(szuletesiEv)
kiiratás(felhasználoNev, kor)




