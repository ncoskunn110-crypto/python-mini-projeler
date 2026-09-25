butce = 1000
can = 5

alisveris_listesi = ["çanta", "kitap", "parfüm"]
borclar = 350
fiyatlar = [500, 200, 300]

giris_basarili = False

while True:

    sifre = input("şifreyi yazınız: ")

    if sifre == "mayhomvan":
        print("Doğru girdiniz, ilerleyebilirsiniz.")
        giris_basarili = True
        break

    else:
        print("Şifreyi yanlış girdiniz, tekrar deneyin.")
        can -= 1

        if can == 0:
            print("Hakkınız kalmadı.")
            break


if giris_basarili:

    print("\n---- ana menü ----")
    print("1. Bütçeyi gör")
    print("2. Alışveriş listeniz")
    print("3. Listedekilerin fiyatları")
    print("4. Borçlarınız")
    print("5. Alışveriş listesi ile borçların toplam tutarı")
    print("6. Çıkış")

    while True:

        secim = input("Seçiminiz (1/2/3/4/5/6): ")

        if secim == "1":
            print(f"Bütçeniz {butce} TL kadardır. Dikkatli harcayın.")

        elif secim == "2":
            for y in alisveris_listesi:
                print(y)

        elif secim == "3":
            print(f"{fiyatlar[0]}, {fiyatlar[1]}, {fiyatlar[2]}")

        elif secim == "4":
            print(f"{borclar} TL borcunuz vardır.")

        elif secim == "5":
            toplam_tutar = sum(fiyatlar)
            toplam = toplam_tutar + borclar
            print(f"Alışveriş + borç toplamı: {toplam} TL")

        elif secim == "6":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Yanlış seçim, tekrar dene.")








