butce = 1000
can = 5
alisveris_listesi = ["çanta", "kitap", "parfüm"]
borclar = 350
fiyatlar = ["500", "200", "300"]
 
while True:
    sifre = input("şifreyi yazınız:")
    if sifre == "mayhomvan":
        print("doğru girdiniz, ilerleyebilirsiniz.")
        break

    else:
        print("şifreyi yanlış girdiniz tekrar deneyin.")
        can -= 1
        
        if can == 0:
            print("Hakkınız kalmadı.")
            break


print("\n----ana menü----")
print("1. bütçeyi gör")
print("2. alışveriş listeniz")
print("3. listedekilerin fiyatları:")
print("4. borçlarınız")
print("5. alışveriş listesi ile borçların toplam tutarı")
print("6.  çıkış")

while True:

    secim = input("seçiminiz(1/2/3/4/5/6):")


    if secim == "1":
        print(f"bütçeniz {butce} TL kadardır. dikkatli harcayın. ")

    elif secim == "2":
        for y in alisveris_listesi:
            print(y)

    elif secim == "3":
         print(f"{fiyatlar[0]}, {fiyatlar[1]}, {fiyatlar[2]}")


    elif secim == "4":
        print(f"{borclar} bu kadardır.")

    elif secim == "5":
        toplam_tutar = int(alisveris_listesi)
        toplam_tutar2 = int(borc)
        print(toplam_tutar + toplam_tutar2)

        toplam_tutar = sum(fiyatlar)
        toplam = toplam_tutar + borclar
        print(f"Toplam tutar: {toplam} TL")

    elif secim == "6":
            print("programdan çıkılıyor..")
            break
    else:
            print("yanlış seçim, tekrar dene.")
            continue









