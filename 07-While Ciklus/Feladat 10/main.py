
#10- Kérjünk be egy max 2 jegyű, pozitív n számot:
	#Írjuk ki 0 és n közt a páros számokat
	#Adjuk össze 0 és n közt az 5-el osztható számokat
	#Számoljuk meg, hány szám osztható 0 és n közt 11-el
	#Írjuk ki azon számokat 0 és n közt amelyek 7-el osztva 3-at adnak maradékul

import os
import time

n:int=None
nData:str=""
ottelOszthato:int=0
szamokSzama:int=0

while(n==None or n>99 or n<0):
    nData=input("Adjon meg egy maximum 2 jegyű pozitív számot: ")

    if(nData.replace("-","").isnumeric()):
        n=int(nData)

        if(n>99 or n<0):
            print("Rosz számot adtál meg")
            time.sleep(3)
            os.system("cls")
print("A páros számok: ")
for i in range(0, n+1, 1):
    if(i%2==0):
        print(f"{i}", end=" ")  
    if(i%5==0):
        ottelOszthato+=1
    if(i%11==0):
        szamokSzama+=1
print(f"\nAz 5 osztható számok száma: {ottelOszthato}")
print(f"Az 11 osztható számok száma: {szamokSzama}")
print("A 7 el osztott számok amiknek a maradéka 3:")
for j in range(0, n+1, 1):
    if(j%7==3):
        print(f"{j}", end=" ")



