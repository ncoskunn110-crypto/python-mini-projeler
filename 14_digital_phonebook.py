rehber = {
    "ahmet yilmaz": "5555512345",
    "ayse demir": "5555556789",
    "mehmet kaya": "555519873"
}

print("---dijital telefon rehberi---")

while True:
    print("\n1. rehberi listele")
    print("2. kişi ekle")
    print("3 isme gore ara")
    print("4. çıkış")

    secim = input("seçiminiz (1/2/3/4):")

    if secim == "1":
        print("\n---rehber listesi---")
        for isim, tel in rehber.items():
            print(f"{isim.title()} : {tel}")

    elif secim == "2":
        isim = input("ad soyad:").lower()
        tel = input("telefon numarası:") 
        rehber[isim] = tel
        print(f"'{isim.title()}' listeye eklendi.")

    elif secim == "3":
        aranan = input("aranacak ifade (örn: ah , yilmaz):").lower()
        bulunan_sayisi = 0

        print("\narama sonuçları")
        for isim, tel in rehber.items():
            if aranan in isim:
                print(f"-> {isim.title()} : {tel}")
                bulunan_sayisi += 1

        if bulunan_sayisi == 0:
            print("eşleşen kayıt bulunamadı.")

    elif secim == "4":
        print("rehber kapatılıyor.")
        break
    else:
        print("geçersiz seçim.")



