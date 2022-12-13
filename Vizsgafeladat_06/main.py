class Balkezes():
    def __init__(self,filename):
        self.filename=filename
        self.adat={}
        self.adatok=[]
        self.adatfeltoltes()

    def adatfeltoltes(self):
        with open(self.filename,"r") as file:
            fejlec=file.readline().strip().split(";")
            for elem in file:
                sor=elem.strip().split(";")
                self.adat[fejlec[0]] = sor[0]
                self.adat[fejlec[1]] = sor[1]
                self.adat[fejlec[2]] = sor[2]
                self.adat[fejlec[3]] = sor[3]
                self.adat[fejlec[4]] = sor[4]
                self.adatok.append(self.adat)
                self.adat={}

    def printer(self,feladat_szam,tömb):
        print (f"Eredemény a {feladat_szam} feladatra: ")
        for elem in tömb:
            print (elem)

    def harmadik_feladat(self):
        adatok_hosszusaga = []
        adatok_hosszusaga.append(len(self.adatok))
        self.printer(3,adatok_hosszusaga)

    def negyedik_feladat(self):
        eredmeny=[]
        for elem in self.adatok:
            if (elem["utolsó"] < "1999-10-31") and (elem["utolsó"] > "1999-10-01"):
                eredmeny.append(f"{elem['név']},{float(elem['magasság'])*2.54:.1f} cm")
        self.printer(4,eredmeny)

    def otodik_feladat(self):
        while True:
            bemenet = str(input("Kerek egy evszamot 1990 és 1999 között: "))
            if (bemenet >= "1990") and (bemenet <= "1999"):
                return bemenet
            else:
                print ("Hibás adat! Kerek egy evszamot 1990 és 1999 között: ")

    def hatodik_feladat(self):
        sulyok=[]
        osszeg = 0
        evszam=self.otodik_feladat()
        for elem in self.adatok:
            if evszam in elem["első"]:
                sulyok.append(int(elem["súly"]))
        for elem in sulyok:
            osszeg+=elem
        eredmeny=osszeg / len(sulyok)
        self.printer(6,[eredmeny])

balkezes=Balkezes("balkezesek.csv")
balkezes.harmadik_feladat()
balkezes.negyedik_feladat()
#balkezes.otodik_feladat()
balkezes.hatodik_feladat()