import os
import time

valasztotUditoData:str=""
valasztotUdito:int=None


while(valasztotUdito==None):
    print("Ital aútómata")
    print("[1]-sprite\n[2]-fanta\n[3]-cola\n")
    valasztotUditoData=input("Melyik üdítőt kéri? ")
    if(valasztotUditoData.replace("-","").isnumeric()):
        valasztotUdito=int(valasztotUditoData)
    else:
        print("Rosz számot adtál meg")
        time.sleep(1)
        os.system("cls")

if(valasztotUdito == 1):
    print("Sprite")
elif(valasztotUdito == 2):
    print("Fanta")
elif(valasztotUdito ==3 ):
    print("Cola")
else:
    print("Nem jó számot adott meg")
    time.sleep(1)
    os.system("cls")

