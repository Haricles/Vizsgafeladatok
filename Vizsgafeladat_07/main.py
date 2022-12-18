class Fuvar():
    def __init__(self,filename):
        self.filename=filename
        self.adat={}
        self.adatok=[]

    def adatbeolvasas(self):
        with open(self.filename,"r",encoding="utf-8-sig") as file:
            fejlec=file.readline().strip().split(";")
            for elem in file:
                sor=elem.strip().split(";")
                sor[3]=sor[3].replace(",",".")
                sor[4]=sor[4].replace(",",".")
                sor[5]=sor[5].replace(",",".")
                self.adat[fejlec[0]] = int(sor[0])
                self.adat[fejlec[1]] = sor[1]
                self.adat[fejlec[2]] = int(sor[2])
                self.adat[fejlec[3]] = float(sor[3])
                self.adat[fejlec[4]] = float(sor[4])
                self.adat[fejlec[5]] = float(sor[5])
                self.adat[fejlec[6]] = sor[6]
                self.adatok.append(self.adat)
                self.adat={}
        return self.adatok

    def bevetel_meghatarozas(self,id):
        bevetel=0
        fuvarok_szama=0
        for elem in self.adatok:
            if elem["taxi_id"] == id:
                bevetel+=float(elem["viteldij"])
                fuvarok_szama+=1
        return f"4.feladat:{fuvarok_szama} fuvar alatt: {bevetel} $"

    def fizetesi_modok(self):
        fizetesi_mod={}
        for elem in self.adatok:
            if elem["fizetes_modja"] not in fizetesi_mod:
                fizetesi_mod[elem["fizetes_modja"]]=1
            else:
                fizetesi_mod[elem["fizetes_modja"]] += 1
        return fizetesi_mod

    def osszesitett_kilometer(self):
        ossz_km=0
        for elem in self.adatok:
            ossz_km += elem["tavolsag"]*1.6
        return round(ossz_km,2)

    def leghosszabb_idotartam_ut_adatai(self):
        leghosszabb=0
        for elem in self.adatok:
            if elem["idotartam"] > leghosszabb:
                leghosszabb=elem["idotartam"]
        for elem in self.adatok:
            if leghosszabb== elem["idotartam"]:
                return f"Leghosszabb fuvar:\n Fuvar hossza: {elem['idotartam']} masodperc\n Taxi azonositó: {elem['taxi_id']}\n" \
                       f" Megtett tavolsag: {elem['tavolsag']}\n Vitel dija: {elem['viteldij']}\n"

    def adat_exportalas(self):
        with open("hibak.txt","w",encoding="utf-8") as kimenet:
            for elem in self.adatok:
                if elem["idotartam"] > 0 and elem["viteldij"] > 0 and elem["tavolsag"]== 0:
                    kimenet.write(str(elem)+"\n")

fuvar=Fuvar("fuvar.csv")
fuvar.adatbeolvasas()
print (fuvar.bevetel_meghatarozas(6185))
print (fuvar.fizetesi_modok())
print (fuvar.osszesitett_kilometer())
print (fuvar.leghosszabb_idotartam_ut_adatai())
fuvar.adat_exportalas()