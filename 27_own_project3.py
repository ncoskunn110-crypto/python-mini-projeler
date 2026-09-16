manav_listesi = []
butce = 360

print("markette neler alman gerektiğinin listesi")
print("1. alman gerekenleri ekle")
print("2. alman gerekenlerin fiyatlarını incele")
print("3. alınması gerekenler alındıktan sonra elde kalan tutarı incele")
print("4. elde kalan tutarla alıp alamayacaklarını gör")
print("5. çıkış")

while True:
    secim = input("seçiminiz nedir(1/2/3/4/5/6):")

    if secim == "1":
        liste = input(" ne eklemek istiyorsun?:").split()
          
        if len(liste) > 4:
            print("maximum 4 farklı ürün alabilirsin.")

        else:
            manav_listesi.extend(liste)
            print(f"Eklediklerin: {manav_listesi}")

    elif secim == "2":
        fiyatlar = [35, 55, 60, 30]
        for i in range(len(manav_listesi)):
             print(f"{manav_listesi[i]}: {fiyatlar[i]} TL")

    elif secim == "3":
        fiyatlar = [35, 55, 60, 30]
        toplam_tutar = sum(fiyatlar[:len(manav_listesi)])
        print(f"Toplam tutar: {toplam_tutar} TL")

    elif secim == "4":
        fiyatlar = [35, 55, 60, 30]
        toplam_tutar = sum(fiyatlar[:len(manav_listesi)])
        kalan = butce - toplam_tutar
        print(f"kalan bütçeniz {kalan} TL kadardır.")

        alinacaklar = input( "Kalan bütçeyle 100 TL'ye 'bardak', " "80 TL'ye 'kitap', 90 TL'ye 'suluk' alabilirsiniz. " "Seçiminiz nedir?: " ).split()

        bardak = 100
        kitap = 80
        suluk = 90
         
        if "kitap" in alinacaklar and "suluk" in alinacaklar: 
                toplam1 = sum([kitap, suluk])
                print(f"Toplam {kitap + suluk} TL'lik alışveriş daha yaptınız.")

        elif "kitap" in alinacaklar and "bardak" in alinacaklar:
                toplam2 = sum([kitap, bardak])
                print(f" toplam {kitap + bardak} TL'lik alışveriş daha yaptınız.")

        elif "kitap" in alinacaklar:
                toplam3 = 80
                print(f"toplam {kitap} TL alışveriş daha yaptınız")

        elif "bardak" in alinacaklar:
                toplam4 = 100
                print(f"toplam {bardak} TL alışveriş daha yaptınız.")

        elif "suluk" in alinacaklar:
                toplam5 = 90
                print(f"toplam {suluk} TL alışveriş daha yaptınız.")

        else:
                print("paranız ikisini ya da üçünü almaya yetmiyor.")

    elif secim == "5":
        print("programdan çıkılıyor...")
        break

   



            








