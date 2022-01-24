ottelOszthatoSzamokOsszege:int=0
hettelOszthatoSzamokOsszege:int=0

print("Kezdőértek=")
kezdErtek:int=int(input())
print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdErtek, vegErtek, 1):
    ottelOszthatoSzamokOsszege+=i
    if(i%5==0 and i%7==0):
        hettelOszthatoSzamokOsszege+=i
        ottelOszthatoSzamokOsszege+=i
    elif(i%7==0):
        hettelOszthatoSzamokOsszege+=i
    elif(i%5==0):
        ottelOszthatoSzamokOsszege+=i
if(ottelOszthatoSzamokOsszege>hettelOszthatoSzamokOsszege):
    print("Az öttel osztható számok összege több")
elif(ottelOszthatoSzamokOsszege<hettelOszthatoSzamokOsszege):
    print("A héttel osztható számok összege több")
else:
    print("A számok összge egyenlő")