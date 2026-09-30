
ogrenciler1 = {
    "ahmet": 75,
    "selin": 90,
    "yagiz": 65,
    "nehir": 85
}

ogrenciler2 = {
    "ahmet": 24,
    "selin": 35,
    "yagiz": 78,
    "nehir": 87
}


def not_getir1(isim):
    return ogrenciler1[isim]


def not_getir2(isim):
    return ogrenciler2[isim]


def ortalama_hesapla(isim):
    not1 = ogrenciler1[isim]
    not2 = ogrenciler2[isim]

    return (not1 + not2) / 2


print("1. ahmetin notu")
print("2. selinin notu")
print("3. yagizin notu")
print("4. nehirin notu")


isim = input(
    "1. dönem notunu görmek istediğiniz öğrenci adı "
    "(ahmet, selin, yagiz, nehir): "
).lower()

if isim in ogrenciler1:
    sonuc = not_getir1(isim)
    print("1. dönem notu:", sonuc)
else:
    print("Öğrenci bulunamadı.")


isim2 = input(
    "2. dönem notunu görmek istediğiniz öğrenci adı "
    "(ahmet, selin, yagiz, nehir): "
).lower()

if isim2 in ogrenciler2:
    sonuc = not_getir2(isim2)
    print("2. dönem notu:", sonuc)
else:
    print("Öğrenci bulunamadı.")


isim3 = input(
    "2 notun ortalamasını görmek için 'b' ye basın: "
).lower()

if isim3 == "b":

    secim = input(
        "Hangi öğrencinin ortalamasını görmek istiyorsunuz "
        "(ahmet, selin, yagiz, nehir): "
    ).lower()

    if secim in ogrenciler1:
        sonuc = ortalama_hesapla(secim)
        print("Ortalama:", sonuc)
    else:
        print("Öğrenci bulunamadı.")














