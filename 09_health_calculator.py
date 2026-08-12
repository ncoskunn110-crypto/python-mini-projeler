print("\n---sağlık ve kalori hesaplama asistanı---")

while True:
    print("\n1.Vücut Kitle İndeksi (VKİ) ve Kalori Hesapla")
    print("2. çıkış")

    secim = input("seçiminiz: (1/2)")  

    if secim =="2":
        print("saglıklı gunler dılerız, gorusmek uzere")
        break

    if secim == "1":
        try:
            kilo = float(input("kilonuz, (kg, örn :70 kg):"))
            boy = float(input("boyunuz: (metre cinsinden, örn:1.65 ):"))
            yas = int(input("yaşınız:"))
            cinsiyet = input("cinsiyetiniz ( E/K): ").upper()

            print("\nhareket seviyeniz: ")
            print("1. hareketsiz iş(masa başı iş)")
            print("2. az hareketli (haftada 1-2 spor)")
            print("3. orta hareketli (haftada 3-4 spor)")
            print("4. çok hareketl iş (her gün spor/yoğun tempo)")
            hareket_secim = input("seçiminiz (1/2/3/4): ")
        except ValueError:
            print("Hatalı veri girdin! Lütfen sayısal değerleri doğru formatta gir.")
            continue
        vki = kilo / (boy ** 2)
        print("\n---sonuçlarınız---")
        print(f"vucut kilo endeksiniz: {vki:.2f}")

        if vki < 18.5:
            print("durumunuz: zayıf")
        elif 18.5 <= vki < 25:  
            print("durumunuz: normal")
        elif 25 <= vki < 30:
            print("durumunuz: kilolu")
        else:
            print("durumunuz: obez")

        if cinsiyet == 'E':
           bmr = 88.36 + (13.4 * kilo) + (4.8 * (boy * 100)) - (5.7 * yas)
        else:
            bmr = 447.6 + (9.2 * kilo) + (3.1 * (boy * 100)) - (4.3 * yas)

        carpanlar = {"1": 1.2, "2": 1.375, "3": 1.55, "4": 1.725}

        if hareket_secim in carpanlar:
            gunluk_kalori = bmr *carpanlar[hareket_secim] 
            print(f"gunluk kalori ihtiyacınız: {gunluk_kalori:.0f} kcal")   
        else:
            print("hareket seviyesini yanlış yazdığınız için hesaplanamadı") 
    else:
        ("geçersiz seçim tekrar dene")


