sozluk = {
    "apple":"elma",
    "computer":"bilgisayar",
    "python": "yilan programlama dili"
}

while True:
    print("\n---KELİME SOZLUGU---")
    print("1.kelimeyi ekle")
    print("2. kelime ara (çeviri)")
    print("3.tüm sözlüğü göster")
    print("4. kelime sil")
    print("5. çıkış")

    secim = input("seçiminiz (1/2/3/4/5): ")

    if secim == "1":
        ingilizce = input("ingilizce kelime:  ").lower()
        turkce = input("türkçe anlamı: ").lower()

        sozluk[ingilizce] = turkce
        print(f"'{ingilizce}' başarıyla eklendi" )

    elif secim == "2":
        aranan = input("hangi kelimenin anlamını arıyorsunuz?: ").lower()

        if aranan in sozluk:
            print(f"anlamı: {sozluk[aranan]}")
        else:
            print("bu kelime sozlukte yok")

    elif secim == "3":
        print("\nsozlukteki tum kelimeler:")
        for ing, turk in sozluk.items():
            print(f"{ing} : {turk}")

    elif secim == "4":
        silinecek = input("silinecek ingilizce kelime:").lower()
        if silinecek in sozluk:
            del sozluk[silinecek]
            print(f"'{silinecek}' sozlukten silindi.")
        else:
            print("bu kelime sozlukte yok")

    elif secim == "5":
        print("sozluk kapatılıyor, gorusmek uzere.")
        break
    else:
        print("geçersiz seçim, yeniden dene.")



