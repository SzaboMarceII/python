harommalOszthatoSzamok:int=0

print("Kezdőértek=")
kezdErtek:int=int(input())
print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdErtek, vegErtek, 1):
    if(i%3==0):
        harommalOszthatoSzamok+=1

print(f"{harommalOszthatoSzamok} szám osztható 3 al")


