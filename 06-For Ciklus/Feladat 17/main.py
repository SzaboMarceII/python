osszeg:int=0
atlag:float=0
szamokSzama:int=0

print("Kezdőértek=")
kezdErtek:int=int(input())
print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdErtek, vegErtek, 1):
    osszeg+=i
    szamokSzama+=1

atlag=osszeg/szamokSzama
print(f"{atlag}")
