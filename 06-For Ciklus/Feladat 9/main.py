print("kezdErtek=")
kezdErtek:int=int(input())
print("vegErtek=")
vegErtek:int=int(input())

if(vegErtek%2!=0):
    vegErtek-=1
    
for i in range(vegErtek, kezdErtek, -2):
    print(i) 