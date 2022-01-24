print("kezdErtek=")
kezdErtek:int=int(input())
print("vegErtek=")
vegErtek:int=int(input())

sum:int=0

szorzat:int=1

for i in range(kezdErtek, vegErtek + 1, 1):
    sum += i
    szorzat *= i

print(f"Az intervallum összege {sum}" )
print(f"Az intervallum szorzata {szorzat}" )
