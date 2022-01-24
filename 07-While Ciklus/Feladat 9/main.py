#Kérjünk be egy 3 jegyű  számot és állapítsuk meg, hogy osztható e 7-el. Addig ismételjük a bekérést, amíg nem 3 jegyű a megadott szám.

import os
import time

beolvasottSzam:int=0
beolvasottSzamData:str=""

while(beolvasottSzam>999 or beolvasottSzam<100):
    beolvasottSzamData=input("Adjon meg egy 3 jegyű számot: ")

    if(beolvasottSzamData.replace("-","").isnumeric()):
        beolvasottSzam=int(beolvasottSzamData)

        if(beolvasottSzam>999 or beolvasottSzam<100):
            print("Rosz számot adtál meg")
            time.sleep(3)
            os.system("cls")

if(beolvasottSzam%7==0):
    print("Osztható 7 el")
else:
    print("Nem osztható 7 el")

