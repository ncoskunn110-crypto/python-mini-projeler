
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
print("3. yagızın notu")
print("4. nehirin notu")

isim = input("1. donem notunu görmek istediğiniz öğrenci adı(ahmet,selin,yagiz, nehir):").lower()
isim2 = input("2. donem notunu görmek istediğiniz öğrenci adı(ahmet,selin,yagiz, nehir):").lower()
isim3 = input("2 notun ortalamasını görmek için b' ye basın:").lower()


if isim in ogrenciler1:
    sonuc = not_getir1(isim)
    print(sonuc)
else:
    print("Öğrenci bulunamadı.")

if isim2 in ogrenciler2:
    sonuc = not_getir2(isim2)
    print(sonuc)
else:
    print("Öğrenci bulunamadı.")

if isim3 == "b":
    secim = input("hangi öğrencinin ortalamasını görmek istiyorsunuz(ahmet,selin,yagiz, nehir):)")
    if secim == "ahmet":
        sonuc = ortalama_hesapla("ahmet")
        print(sonuc)

    elif secim == "selin":
        sonuc = ortalama_hesapla("selin")
        print(sonuc)

    elif secim == "yagiz":
        sonuc = ortalama_hesapla("yagiz")
        print(sonuc)

    elif secim == "nehir":
        sonuc = ortalama_hesapla("nehir")
        print(sonuc)














