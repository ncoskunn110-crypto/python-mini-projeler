manav_listesi = []

butce = 360

print("Markette neler alman gerektiğinin listesi")
print("1. Alman gerekenleri ekle")
print("2. Alman gerekenlerin fiyatlarını incele")
print("3. Alınması gerekenler alındıktan sonra elde kalan tutarı incele")
print("4. Elde kalan tutarla alıp alamayacaklarını gör")
print("5. Çıkış")

fiyatlar = [35, 55, 60, 30]

while True:

    secim = input("Seçiminiz nedir (1/2/3/4/5): ")

    if secim == "1":

        liste = input("Ne eklemek istiyorsun?: ").split()

        if len(manav_listesi) + len(liste) > 4:
            print("Maksimum 4 farklı ürün alabilirsin.")

        else:
            manav_listesi.extend(liste)
            print(f"Eklediklerin: {manav_listesi}")

    elif secim == "2":

        for i in range(len(manav_listesi)):
            print(f"{manav_listesi[i]}: {fiyatlar[i]} TL")

    elif secim == "3":

        toplam_tutar = sum(fiyatlar[:len(manav_listesi)])
        kalan = butce - toplam_tutar

        print(f"Toplam tutar: {toplam_tutar} TL")
        print(f"Kalan bütçeniz: {kalan} TL")

    elif secim == "4":

        toplam_tutar = sum(fiyatlar[:len(manav_listesi)])
        kalan = butce - toplam_tutar

        print(f"Kalan bütçeniz: {kalan} TL")

        alinacaklar = input(
            "Kalan bütçeyle "
            "100 TL'ye bardak, "
            "80 TL'ye kitap, "
            "90 TL'ye suluk alabilirsiniz. "
            "Seçiminiz nedir?: "
        ).split()

        bardak = 100
        kitap = 80
        suluk = 90

        ek_alısveris = 0

        if "bardak" in alinacaklar:
            ek_alısveris += bardak

        if "kitap" in alinacaklar:
            ek_alısveris += kitap

        if "suluk" in alinacaklar:
            ek_alısveris += suluk

        if ek_alısveris == 0:
            print("Geçerli bir ürün seçmediniz.")

        elif ek_alısveris <= kalan:
            print(f"Toplam {ek_alısveris} TL'lik alışveriş daha yaptınız.")
            kalan -= ek_alısveris
            print(f"Alışverişten sonra kalan bütçeniz: {kalan} TL")

        else:
            print("Bu ürünleri almaya bütçeniz yetmiyor.")

    elif secim == "5":

        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim.")
   



            








