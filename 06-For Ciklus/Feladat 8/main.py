print("kezdErtek=")
kezdErtek:int=int(input())
print("vegErtek=")
vegErtek:int=int(input())

if(kezdErtek%2==0):
    kezdErtek+=1
    
for i in range(kezdErtek, vegErtek, 2):
    print(i) 