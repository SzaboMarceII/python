parosSzamokOsszege:int=0
paratlanSzamokOsszege:int=0


print("Kezdőértek=")
kezdErtek:int=int(input())
print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdErtek, vegErtek, 1):
    parosSzamokOsszege+=i
    if(i%2==0):
            parosSzamokOsszege+=i
    else:
        paratlanSzamokOsszege+=i
if(parosSzamokOsszege>paratlanSzamokOsszege):
    print("A párosak összege több")
else:
    print("A páratlan számok össszeg nagyobb")



