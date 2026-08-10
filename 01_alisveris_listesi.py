alisveris_listesi = []

while True:
    print("\n---Alışveriş Listesi---")
    print("1. Ürünü Ekle")
    print("2. Listeyi Göster")
    print("3. ürünü sil")
    print("4.çıkış")

    secim = input("seçiminiz (1/2/3/4): ")
    if secim == "1":
        urun = input("eklenecek ürün: ")
        alisveris_listesi.append(urun)
        print(f"'{urun}' listeye eklendi.")
     
    elif secim == "2":
        print("\nlistendeki ürünler:")
        if len(alisveris_listesi) == 0:
            print("listeniz boş.")
        else:
            for sira, urun in enumerate(alisveris_listesi, 1):
                print(f"{sira}. {urun}")

    elif secim == "3":
        urun = input("silinecek ürün:")
        if urun in alisveris_listesi:
            alisveris_listesi.remove(urun)
            print("'{urun}' listeden silindi.")
        else:
            print("bu ürün zaten listede yok.")

    elif secim == "4":
        print("programdan çıkılıyor görüşmek üzere.")
        break
    else:
        print("geçersiz seçim, 1 2 veya 3 yazın") 
