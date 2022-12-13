from pprint import pprint

szotar={}
adatok=[]
with open("jackie.txt","r",encoding="utf-8") as file:
    adat=file.readline().strip().split()
    for elem in file:
        sor=elem.strip().split()
        szotar[adat[0]] = sor[0]
        szotar[adat[1]] = int(sor[1])
        szotar[adat[2]] = int(sor[2])
        szotar[adat[3]] = int(sor[3])
        szotar[adat[4]] = int(sor[4])
        szotar[adat[5]] = int(sor[5])
        adatok.append(szotar)
        szotar={}
print (f"3.feladat: {len(adatok)}")

legtöbb=adatok[0]["races"]
for elem in adatok:
    if legtöbb < elem["races"]:
        legtöbb=elem["races"]

for elem in adatok:
    if legtöbb == elem["races"]:
        print (f'4.feladat: {elem["year"]}')

nyert_versenyek_6=0
nyert_versenyek_7=0
print ("5.feladat:")
for elem in adatok:
    if int(elem["year"][2]) == 6:
        nyert_versenyek_6+=elem["wins"]
    else:
        nyert_versenyek_7+=elem["wins"]

print (f"70-es évek: {nyert_versenyek_7} megnyert verseny")
print (f"60-es évek: {nyert_versenyek_6} megnyert verseny")



