osszeg:int=0
elojelValto:int=1

print("Kezdőértek=")
kezdErtek:int=int(input())
print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdErtek, vegErtek+1, 1):
    osszeg=osszeg+-i*elojelValto
    elojelValto=elojelValto*-1
print(f"{osszeg}")

