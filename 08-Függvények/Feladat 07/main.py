#7 - A program bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy érdemjegyet az alábbiak szerint! : 
# 1: x<50; 
# 2: 50<=x<60; 
# 3: 60<=x<70; 
# 4: 70<=x<85; 
# 5: x>=85.

import os 
import time

#hiba
def hiba(uzenet:str)->None:
    print(uzenet)
    time.sleep(3)
    os.system("cls")

#pontszam bekerese 
def pontBekeres()->int:
    pontSzam:int=None
    while(pontSzam==None):
        data:str=input("Kérem a pontszámot: ")
        if(data.isdigit()):
            pontSzam=int(data)
            if(pontSzam>=0 and pontSzam <=100):
                return pontSzam
            else:
                pontSzam=None
                print("0 és 100 között adjon meg értéket!")
        else:
            hiba("Nem számot adott meg")
        
#pontszam vizsgálatat
def pontszamVizsgalat(szam:int)->int:
    if(szam<50):
        return 1
    elif(szam<=50 and szam>60):
        return 2
    elif(60<=szam and szam<70):
        return 3
    elif(70<=szam and szam<85):
        return 4
    else:
        return 5
#kiírás
def kiiras(pontSzam:int, erdemjegy:int)->None:
    print(f"Az ön pontszáma: {pontSzam}\nAz érdemjegye: {erdemjegy}")

#főprogram
pontSzam:int=pontBekeres()
erdemjegy:int=pontszamVizsgalat(pontSzam)
kiiras(pontSzam, erdemjegy)
