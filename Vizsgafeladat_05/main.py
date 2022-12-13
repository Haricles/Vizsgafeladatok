adat={}
adatok=[]
with open("eredmenyek.csv","r") as file:
    fejlec=file.readline().strip().split(";")
    for elem in file:
        sor=elem.strip().split(";")
        adat[fejlec[0]] = sor[0]
        adat[fejlec[1]] = sor[1]
        adat[fejlec[2]] = sor[2]
        adat[fejlec[3]] = sor[3]
        adat[fejlec[4]] = sor[4]
        adat[fejlec[5]] = sor[5]
        adatok.append(adat)
        adat={}

hazai=0
idegen=0
for elem in adatok:
    if elem["hazai"]=="Real Madrid":
        hazai+=1
    if elem["idegen"]=="Real Madrid":
        idegen+=1

print (f"3.feladat: Real Madrid: Hazai: {hazai} , Idegen: {idegen}")


volt_dontetlen=True
for elem in adatok:
    if elem["hazai_pont"] == elem["idegen_pont"] and volt_dontetlen:
        volt_dontetlen=True
    else:
        volt_dontetlen=False

if volt_dontetlen:
    print ("Volt dontetlen? igen")
else:
    print ("Volt dontetlen? nem")

teljes_nev=""
for elem in adatok:
    if "Barcelona" in elem["hazai"]:
        teljes_nev=elem["hazai"]

print (f"5.feladat: A barcelonai csapat neve: {teljes_nev}")


for elem in adatok:
    if elem["időpont"] == "2004-11-21":
        print (f"{elem['hazai']}-{elem['idegen']} ({elem['hazai_pont']}:{elem['idegen_pont']})")

stadion_szamlalo={}
for elem in adatok:
    if elem["helyszín"] not in stadion_szamlalo:
        stadion_szamlalo[elem["helyszín"]] = 1
    else:
        stadion_szamlalo[elem["helyszín"]] += 1

for key,value in stadion_szamlalo.items():
    if value > 20:
        print (f"{key}: {value}")
