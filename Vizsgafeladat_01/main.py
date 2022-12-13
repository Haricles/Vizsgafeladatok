from pprint import pprint
szotar={}
adatok=[]
with open("kolcsonzesek.txt","r",encoding="utf-8") as file:
    kulcsok=file.readline().strip().split(";")
    for adat in file:
        sor=adat.strip().split(";")
        szotar[kulcsok[0]] = sor[0]
        szotar[kulcsok[1]] = sor[1]
        szotar[kulcsok[2]] = int(sor[2])
        szotar[kulcsok[3]] = int(sor[3])
        szotar[kulcsok[4]] = int(sor[4])
        szotar[kulcsok[5]] = int(sor[5])
        adatok.append(szotar)
        szotar={}
#5.feladat:
print (f"Napi kölcsönzések száma: {len(adatok)}")

#6.feladat:
nev_bemenet="Kata"
szamlalo=0
print(f"{nev_bemenet} kölcsönzései:")
for elem in adatok:
    if elem["Név"]==nev_bemenet:
        print (f'{elem["EÓra"]}:{elem["EPerc"]}-{elem["VÓra"]}:{elem["Vperc"]}')
    else:
        szamlalo+=1
if szamlalo== len(adatok):
    print ("Nem volt ilyen nevű kölcsönző")

#7.feladat:
def atvalt(ora,perc):
    mp=ora*3600 + perc*60
    return mp

ora=10
perc=9
print ("A vízen lévő járművek: ")
for elem in adatok:
    if (atvalt(elem["EÓra"],elem["EPerc"]) < atvalt(ora,perc)) and (atvalt(elem["VÓra"],elem["Vperc"]) > atvalt(ora,perc)):
        print (f'{elem["EÓra"]}:{elem["EPerc"]}-{elem["VÓra"]}:{elem["Vperc"]}: {elem["Név"]}')

#9.feladat:
with open("F.txt","w",encoding="utf-8") as kimenet:
    for elem in adatok:
        if elem["JAzon"]=="F":
            kimenet.write(f'{elem["EÓra"]}:{elem["EPerc"]}-{elem["VÓra"]}:{elem["Vperc"]} : {elem["Név"]}\n')

#10.feladat:
szamlalo_szotar={}
for elem in adatok:
    if elem["JAzon"] not in szamlalo_szotar:
        szamlalo_szotar[elem["JAzon"]]=1
    else:
        szamlalo_szotar[elem["JAzon"]] += 1

print ("Statisztika:")
for key in sorted(szamlalo_szotar):
    print (f"{key}-{szamlalo_szotar[key]}")

