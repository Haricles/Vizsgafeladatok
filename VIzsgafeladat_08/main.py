morzeabc={}
with open("morzeabc.txt","r") as file:
    fejlec=file.readline().strip().split(";")
    for elem in file:
        sor=elem.strip().split()
        if sor[0] not in morzeabc:
            morzeabc[sor[0]]=sor[1]

with open("morze.txt","r") as bemenet:
    for i in bemenet:
        szerzo_idezet=i.strip().split(";")
        szokoz=i.strip().split("       ")

    def sztring_morzekodda(sztring):
        uj_sztring=""
        for elem in sztring:
            if elem.upper()==" ":
                uj_sztring+="       "
            for key,value in morzeabc.items():
                if elem.upper()==key:
                    uj_sztring+=value+" "
        print (f"A megadott sztring morze kódja: {uj_sztring}")

    def morze_dekodolo(kod):
        uj_sztring=""
        kod=kod.split()
        for karakter in kod:
            for key,value in morzeabc.items():
                if karakter==value:
                    uj_sztring+=key+" "
        print (uj_sztring)


sztring_morzekodda("szia mizu van veled")
morze_dekodolo(".-   .-.   ..   ...   --..   -   ---   -   .   .-..   ..-..   ...   --..   ")