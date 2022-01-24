#csomagok importálása
import os
#import keyboard
import time

#változók definiálása

#a szám amit be kell olvasni
#kezdőértéke a none, mivel a while ciklusban ki tudom ezt használni az ismétlések vizsgálatára,
#vagyis a ciklust mindaddug futtatjk, még a number változónak nem lesz szám értéke
number: int=None
#segéd változó, a beolvasott értéket fogja tárolni
data: str=""

#while ciklus, ami mindaddig fog futni meg a number változó nem kap szám értéket, azaz az értéke nem None lesz
while(number==None):
    #beolvasás a konzolról és a beolvasott értéket eltároljuk a data változóba
    data=input("kerem a szamot:")
    #megvizsgáljuk, hogy a beolvasott érték (string) számra alakítható e
    #mindegy hogy ez a szám int vagy float típusú

    #isdigit()->bool változót ad vissza
    if(data.isdigit()):
        #ha az isdigit() fügvény értéke igaz, akkor számot írt be a felhasználó
        #amit mi BIZTOS át tudunk szám típussá alakítani
        number=int(data)
    #az isdigit()függvény értéke hamis, azaz a felhsználó nem számot írt be
    #így a number változó értéke továbbra is none marad, azaz a felhsználó számot írt be
    #a ciklust ismételni kell
    else:
        print("\nNem szamot adott meg!")
        #a programot futtató szálat (therd) elaltatjuk 3 másodpercre
        time.sleep(3)
        # letöröljük a képernyőt
        os.system("cls")


        #print("\nA folytatáshoz nyomja meg az ENTER billentyűt.")
        # egy végtelen WHILE ciklust írunk, mivel arra fogunk várni, hogy a felhasználó
        # lenyomja a kért billenytűzetet (ENTER)
        #while(True):
        #figyeljük, hogy a felhasználó lenyomta e az ENTER gombot
            #if(keyboard.is_pressed('enter')):
            #letöröljük a képernyőt
                #os.system("cls")
                #kilépünk a belső (végtelen) while ciklusból 
                #break

#kiírjuk a beolvasott számot
print(f"A beolvasott szam {number}")