paratlan:int=0

print("Kezdőértek=")
kezdErtek:int=int(input())
print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdErtek, vegErtek, 1):
    if(i%2!=0 and i%3==0):
        paratlan+=1
        
print(f"{paratlan}")
