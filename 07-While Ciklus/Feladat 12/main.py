#12 - Van egy kis megtakarított pénzem (min 10.000, max 50.000). 
#Arra vagyok kíváncsi, hogy hány hónap múlva éri el ez az összeg a bankban a 100 000 Ft-ot, ha havi 2%-os kamattal számolhatok?

import os
import time

penz:float=None
penzData:str=""
honapok:int=0

while(penz==None or penz<10000 or penz>50000):
    penzData=input("Kérek egy számot 10000 és 50000 között: ")
    if(penzData.isnumeric()):
        penz=float(penzData)
    else:
        print("Rosz számot adott meg")
        time.sleep(3)
        os.system("cls")

while(penz<100000):
    penz=penz*1.02
    honapok+=1
print(f"{honapok} Ennyi hónap múlva éri el a pénz 2% kamattal a 100000 forintot")
