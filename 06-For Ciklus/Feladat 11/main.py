parosSzamokOsszege:int=0
paratlanSzamokSzorzata:int=1

print("Kezdőértek=")
kezdErtek:int=int(input())
print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdErtek, vegErtek+1, 1):
    if(i%2==0):
        parosSzamokOsszege+=i
    else:
        paratlanSzamokSzorzata*=i
        
print(f"Az intervallum összege {parosSzamokOsszege}")
print(f"Az intervallum összege {paratlanSzamokSzorzata}")    
