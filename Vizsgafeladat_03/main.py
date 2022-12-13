adat={}
adatok=[]
with open("pilotak.csv","r",encoding="utf-8") as file:
    fejlec = file.readline().strip().split(";")
    for elem in file:
        sor=elem.strip().split(";")
        adat[fejlec[0]] = sor[0]
        adat[fejlec[1]] = sor[1]
        adat[fejlec[2]] = sor[2]
        adat[fejlec[3]] = sor[3]
        adatok.append(adat)
        adat={}

print (f"3.feladat: {len(adatok)}")
print ("4.feladat:",adatok[-1]["\ufeffnev"])

print ("5.feladat:")
for elem in adatok:
    if elem["születési_dátum"]< "1901.01.01":
        print ("\t"+elem["\ufeffnev"],elem["születési_dátum"])

rajtszamok=[]
for elem in adatok:
    if elem["rajtszám"]:
        rajtszamok.append(int(elem["rajtszám"]))

legkisebb=rajtszamok[0]
for elem in rajtszamok:
    if legkisebb>elem:
        legkisebb=elem

for elem in adatok:
    if elem["rajtszám"]== str(legkisebb):
        print (f"6.feladat: {elem['nemzetiség']}")

ismetelt_rajtszamok=[]
egyszer_szerepelt_rajtszamok=[]
for elem in adatok:
    if elem["rajtszám"]== "":
        continue
    if elem["rajtszám"] and (elem["rajtszám"]not in egyszer_szerepelt_rajtszamok):
        egyszer_szerepelt_rajtszamok.append(elem["rajtszám"])
    else:
        ismetelt_rajtszamok.append(elem["rajtszám"])

print (f"7.feladat: {ismetelt_rajtszamok}")



