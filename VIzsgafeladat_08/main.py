def sztring_morzekodda(sztring):
    uj_sztring = ""
    for elem in sztring:
        if elem.upper() == " ":
            uj_sztring += "       "
        for key, value in morzeabc.items():
            if elem.upper() == key:
                uj_sztring += value + " "
    print(f"A megadott sztring morze kódja: {uj_sztring}")

def morze_dekodolo(kod):
    uj_sztring = ""
    kod = kod.split()
    for karakter in kod:
        for key, value in morzeabc.items():
            if karakter == value:
                uj_sztring += key + " "
    print(uj_sztring)

def morze_dekodolo_2(morze_szoveg):
    szoveg = ""
    morze_szoveg = morze_szoveg.replace("   ", ";")
    reszek = morze_szoveg.split(";")
    for karakter in reszek:
        betuk = karakter.split(" ")
        for betu in betuk:
            szoveg+=" "
            for key, value in morzeabc.items():
                if betu == value:
                    szoveg += key
    print(szoveg)

morzeabc={}
with open("morzeabc.txt","r",encoding="ISO-8859-1") as file:
    fejlec=file.readline().strip().split(";")
    for elem in file:
        sor=elem.strip().split()
        if sor[0] not in morzeabc:
            morzeabc[sor[0]]=sor[1]

with open("morze.txt","r",encoding="ISO-8859-1") as bemenet:
    for i in bemenet:
        morze_dekodolo_2(i)


