ogrenci_not_sistemi = []

while True:
    print("\nöğrenci not sistemine hoş geldiniz.")
    print("1. öğrenci eklemek için")
    print("2. öğrencileri göster.")
    print("3. not ekle.")
    print("4. ortalama hesapla.")
    print("5. çıkış")

    secim = input("seçiminiz(1/2/3/4/5):")

    if secim == "1":
            ad = input("eklemek istediğiniz öğrenci adı: ")
            soyad =input("öğrencinin soyadı: ")
            ogrenci_not_sistemi.append([ad, soyad, []])
            print(f"{ad} {soyad} başarıyla eklendi. ")

        
    elif secim == "2":
       for x, y in enumerate(ogrenci_not_sistemi, 1):
            print(f"{x} . {y} ")

    elif secim == "3":
        not_ekle = input("girmek istediğiniz notu ve öğrenci adını yazınız(örn: ali - 50): ")
        ogrenci_not_sistemi.append(not_ekle)
        print(f"{not_ekle} başarıyla eklendi.")
        

    elif secim == "4":
        notlar = input("ortalama hesaplamak istediğiniz 2 notu ayrı ayrı yazınız.(örn: 90 30):").split()
        notlar1 = int(notlar[0])
        notlar2 = int(notlar[1])
        ort = (notlar1 + notlar2) / 2
        print(ort)

    elif secim == "5":
            print("programdan çıkılıyor...")
            break
    else:
            print("lütfen 1-5 arası bir sayı giriniz.")
           





