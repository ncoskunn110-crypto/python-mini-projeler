sepet = []
bakiye = 800

urunler = {
    "elma": 20,
    "ekmek": 15,
    "sut": 30,
    "peynir": 80
}

print("Ürün satın alma simülasyonu")
print("1- Ürünleri gör")
print("2- Ürün seç")
print("3- Seçtiğin üründen miktar belirle")
print("4- Başka ürün ekle")
print("5- Toplam fiyatı gör")

def fiyat_getir(isim):
    return urunler[isim]

def toplam_hesapla(sepet):
    toplam = 0

    for urun in sepet:
        toplam += urunler[urun]

    return toplam


while True:

    secim = input("Seçiminiz (1-2-3-4-5): ")

    if secim == "1":

        for urun, fiyat in urunler.items():
            print(urun, fiyat, "TL")

    elif secim == "2":

        alis = input("Almak istediğiniz ürün adı: ")

        if alis in urunler:
            fiyat = fiyat_getir(alis)
            print(alis, "fiyatı:", fiyat, "TL")

            sepet.append(alis)

        else:
            print("Böyle bir ürün yok.")

    elif secim == "3":

        if len(sepet) == 0:
            print("Henüz sepete bir şey eklenmemiş.")

        else:
            alis = input("Miktarını değiştirmek istediğiniz ürün: ")

            if alis in urunler:

                miktar = int(input("Kaç tane almak istiyorsunuz: "))

                sepet.remove(alis)

                for i in range(miktar):
                    sepet.append(alis)

                fiyat = fiyat_getir(alis)

                print(f"{miktar} adet {alis}: {miktar * fiyat} TL")

            else:
                print("Böyle bir ürün yok.")

    elif secim == "4":

        baska = input("Başka hangi ürünü eklemek istersiniz?: ")

        if baska in urunler:
            fiyat = fiyat_getir(baska)

            print(baska, "fiyatı:", fiyat, "TL")

            sepet.append(baska)

        else:
            print("Böyle bir ürün yok.")

    elif secim == "5":

        sifre = input(
            "Toplam fiyatı görmek için şifrenizi giriniz: "
        )

        if sifre == "mayhomvan":

            print("Şifreniz doğru, sepetinize ulaşılıyor...")

            sonuc = toplam_hesapla(sepet)

            print(f"Toplam borcunuz: {sonuc} TL")

            ode = input("Ödeme yapmak için onaylayınız (e-h): ").lower()

            if ode != "e":
                print("Onaylanmadığı için çıkış yapılıyor.")
                break

            kalan = bakiye - sonuc

            if kalan < 0:
                print("Bakiyeniz bu alışveriş için yetersiz.")
                break

            else:
                print(
                    f"Alışveriş başarıyla tamamlandı. "
                    f"{kalan} TL paranız kaldı."
                )
                break

        else:
            print("Şifre yanlış, yeniden deneyin.")
                   









