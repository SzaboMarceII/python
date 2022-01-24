parosSzamokOsszege:float=0
paratlanSzamokOsszege:float=0
atlag:float=0

print("Kezdőértek=")
kezdErtek:int=int(input())
print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdErtek, vegErtek, 1):
    if(i%2==0):
        parosSzamokOsszege+=i
    else:
        paratlanSzamokOsszege+=i


atlag=parosSzamokOsszege+paratlanSzamokOsszege/2
print(f"{atlag}")
