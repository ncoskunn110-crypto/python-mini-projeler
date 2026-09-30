karakterler = {
    "büyücü": "casanova",
    "savaşçı": "kali",
    "dövüşçü": "vertex",
    "canavar": "fortuna"
}

can = {
    "büyücü": 500,
    "savaşçı": 450,
    "dövüşçü": 700,
    "canavar": 600
}

hasar = { 
    "büyücü": 100,
    "savaşçı": 150,
    "dövüşçü": 70,
    "canavar": 80
}

cephane = []

def tanim(isim):
    return karakterler[isim]

def savas(hero1, hero2):
    guc1 = can[hero1] + hasar[hero1]
    guc2 = can[hero2] + hasar[hero2]

    if guc1 > guc2:
        return hero1
    elif guc2 > guc1:
        return hero2
    else:
        return "berabere"
    

def can_goruntule(cani):
    return can[cani]

print("savaş simulasyonu!!")
print("1- karakterleri görmek")
print("2- karakterlerin adını görmek")
print("3- karakterlerin canını görmek")
print("4- cephaneye ekleyeceğiniz 2 hero")
print("5- seçtiğiniz 2 karakterin vs sonucu kimin kazandığı")
print("6- çıkış")

while True:
    secim  = input("seçiminiz(1-2-3-4-5-6):")

    if secim == "1":
        for hero, ad in karakterler.items():
            print(hero, ad)

    elif secim == "6":
        print("çıkış yapılıyor...")
        break

    elif secim == "2":
        secim1 = input("spesifik olarak görmek istediğiniz heronun adı(örn: büyücü, savaşçı, canavar, dövüşçü):")
        if secim1 in karakterler:
            ad = tanim(secim1)
            print(ad, ":adıdır")
        else:
            print("böyle bir hero karakterler cephanesinde yok")

        secim2 = input("tüm heroların adlarını görmek için e' ye basın:").lower()
        if secim2 != "e":
            print("baslangıca yonlendırılıyorsunuz..")
            break
        else:
            for hero,ad in karakterler.items():
                print(hero, ad)

    elif secim == "3":
        secim3= input("spesifik olarak görmek istediğiniz heronun canı(örn: büyücü, savaşçı, canavar, dövüşçü):")
        if secim3 in can:
            sonuc = can_goruntule(secim3)
            print(sonuc, ":canıdır")
        else:
            print("böyle bir hero karakterler cephanesinde yok ki canına bakalım")

        secim4 = input("tüm heroların canlarını görmek için e' ye basın:").lower()
        if secim4 != "e":
            print("baslangıca yonlendırılıyorsunuz..")
            break
        else:
            for hero,ad in can.items():
                print(hero, ad)

    elif secim == "4":
        hero1 = input("savaşacak 1. heronuzun adı:")
        if hero1 in karakterler:
            print(f" {hero1} cephanenize eklendi")
            cephane.append(hero1)

        else:
            print("bu karakter zaten yok")

        hero2 = input("savaşacak 2. heronun adı:")
        if hero2 in karakterler and hero2 != hero1:
            print(f" {hero2} cephanenize eklendi")
            cephane.append(hero2)
        else:
            print("aynı karakteri ekleyemezsiniz/ böyle bi karakter zaten yok")

    elif secim == "5":
        if len(cephane) == 2:
            sonuc = savas(cephane[0], cephane[1])
            print(f"kazanan {sonuc} !!")
        else: 
            print("cephanede 1 veya daha az ya da 2 'den çok hero olduğundan savaş başlatılamıyor")
            







        






