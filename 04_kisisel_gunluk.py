dosya_adi = "gunluk.txt"
while True:
    print("\n---kişisel günlük---")
    print("1. gunluge yazı ekle")
    print("2.geçmiş notları oku")
    print("3. çıkış")

    secim = input("seçiniz (1/2/3):")

    if secim == "1":
        not_metni = input("bugun ne yazmak istiyorsun? :")
        with open(dosya_adi, "a", encoding="utf-8") as dosya:
            dosya.write(not_metni + "\n")
        print("notunuz basarıyla eklendi")

    elif secim == "2":
        print("\n---geçmiş notların---")

        try:
            with open(dosya_adi, "r", encoding="utf-8") as dosya:
                icerik = dosya.read()
                if icerik == "":
                    print("gunlugun henuz bos")
                else:
                    print(icerik) 
        except FileNotFoundError:
            print("henuz gunluk dosyası yok, once not ekleyin")
    elif secim == "3":
        print("gunluk kapatılıyor, gorusmek uzere.")
        break
    else:
        print("geçersiz seçim yenşden deneyiniz")

