class Feldolgozo():
    def __init__(self,filename):
        self.filename=filename
        self.adat = {}
        self.adatok = []
        self.adatfeltoltes()

    def adatfeltoltes(self):
        with open(self.filename,"r") as file:
            fejlec = file.readline().strip().split(";")
            for elem in file:
                sor = elem.strip().split(";")
                self.adat[fejlec[0]] = sor[0]
                self.adat[fejlec[1]] = sor[1]
                self.adat[fejlec[2]] = sor[2]
                self.adat[fejlec[3]] = sor[3]
                self.adat[fejlec[4]] = sor[4]
                self.adat[fejlec[5]] = sor[5]
                self.adatok.append(self.adat)
                self.adat = {}

    def printer(self,feladat_szam,feladat_szoveg):
        print (f"{feladat_szam}. feladat szövege: ")
        print (f"{feladat_szoveg}")

    def elso_feladat(self):
        hazai=0
        idegen=0
        for elem in self.adatok:
            if elem["hazai"]=="Real Madrid":
                hazai+=1
            if elem["idegen"]=="Real Madrid":
                idegen+=1
        self.printer(1,f"Real Madrid: Hazai: {hazai} , Idegen: {idegen}")

    def masodik_feladat(self):
        volt_dontetlen = True
        for elem in self.adatok:
            if elem["hazai_pont"] == elem["idegen_pont"] and volt_dontetlen:
                volt_dontetlen = True
            else:
                volt_dontetlen = False
        if volt_dontetlen:
            self.printer(2,"Volt dontetlen? Igen")
        else:
            self.printer(2,"Volt dontetlen? Nem")

    def harmadik_feladat(self):
        teljes_nev = ""
        for elem in self.adatok:
            if "Barcelona" in elem["hazai"]:
                teljes_nev = elem["hazai"]
        self.printer(3,f"A barcelonai csapat neve: {teljes_nev}")

    def negyedik_feladat(self):
        self.printer(4,"")
        for elem in self.adatok:
            if elem["időpont"] == "2004-11-21":
                print(f"{elem['hazai']}-{elem['idegen']} ({elem['hazai_pont']}:{elem['idegen_pont']})")

    def ötödik_feladat(self):
        self.printer(5,"")
        stadion_szamlalo = {}
        for elem in self.adatok:
            if elem["helyszín"] not in stadion_szamlalo:
                stadion_szamlalo[elem["helyszín"]] = 1
            else:
                stadion_szamlalo[elem["helyszín"]] += 1
        for key, value in stadion_szamlalo.items():
            if value > 20:
                print(f"{key}: {value}")

acb_kosarlabda=Feldolgozo("eredmenyek.csv")
acb_kosarlabda.elso_feladat()
acb_kosarlabda.masodik_feladat()
acb_kosarlabda.harmadik_feladat()
acb_kosarlabda.negyedik_feladat()
acb_kosarlabda.ötödik_feladat()