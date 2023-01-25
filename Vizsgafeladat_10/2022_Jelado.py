from pprint import pprint
adat={}
adatok=[]
with open ("jel.txt","r",encoding="utf-8") as jelek:
    for jel in jelek:
        sor=jel.strip().split(" ")
        adat["idő"]=sor[0]+":"+sor[1]+":"+sor[2]
        adat["x"]=int(sor[3])
        adat["y"]=int(sor[4])
        adatok.append(adat)
        adat={}

print("2.feladat:")
sor_szam=3
for i,elem in enumerate(adatok):
    if sor_szam==i+1:
        pprint (f"x:{elem['x']} y:{elem['y']}")
        
def eltelt(ido_1,ido_2):
    ido_1=ido_1.split(":")
    ido_2=ido_2.split(":")
    ido_1=list(map(int,ido_1))
    ido_2=list(map(int,ido_2))
    ido_1_masodperc=ido_1[0]*3600+ido_1[1]*60+ido_1[2]
    ido_2_masodperc=ido_2[0]*3600+ido_2[1]*60+ido_2[2]
    masodperc=ido_2_masodperc-ido_1_masodperc
    p,mp = divmod(masodperc,60)
    o,p = divmod(p,60)
    return f"{o}:{p}:{mp}"
    
print (eltelt("3:11:19","22:3:59"))
