adatok=[]
with open("kifejezesek.txt","r") as file:
    for elem in file:
        sor= elem.strip().split()
        adatok.append(sor)

print (f"2.feladat: Kifejezések száma: {len(adatok)}")

szamlalo=0
for elem in adatok:
    if elem[1] == "mod":
        szamlalo+=1

print (f"3.feladat: Kifejezések maradékos osztással: {szamlalo}")

meres=0
for elem in adatok:
    if (int(elem[0]) % 10== 0) and (int(elem[2]) % 10 == 0):
        break
    else:
        meres+=1
if meres == len(adatok):
    print ("4.feladat: Nincs ilyen!")
else:
    print ("4.feladat: Van ilyen kifejezés!")

print (f"5.feladat: Statisztika")
operatorok_szama={}
for elem in adatok:
    if elem[1] not in operatorok_szama:
        operatorok_szama[elem[1]]=1
    else:
        operatorok_szama[elem[1]] +=1

print (f"mod -> {operatorok_szama['mod']}")
print (f" / -> {operatorok_szama['/']}")
print (f"div -> {operatorok_szama['div']}")
print (f"- -> {operatorok_szama['-']}")
print (f"* -> {operatorok_szama['*']}")
print (f"+ -> {operatorok_szama['+']}")


