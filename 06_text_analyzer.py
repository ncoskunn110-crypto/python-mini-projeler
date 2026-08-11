print("---metin analiz araci---")
while True:
    metin = input("lutfen analiz etmek istediginiz metni giriniz (cikmak icin 'q' tusuna basiniz): ")
    
    if metin.lower() == 'q':
        print("programdan cikiliyor, gorusmek uzere!")
        break

    if len(metin.strip()) == 0:
        print("lutfen bos bir metin girmeyiniz")
        continue

    if len(metin) < 10:
        print("lutfen en az 10 karakter uzunlugunda bir metin giriniz")
        continue

    toplam_karakter = len(metin)
    kelimeler = metin.split()
    toplam_kelime = len(kelimeler)

    harf_sayilari = {}

    for harf in metin.lower():
        if harf.isalpha():
            if harf in harf_sayilari:
                harf_sayilari[harf] += 1
            else:
                harf_sayilari[harf] = 1

    
    print("\n--- ANALIZ SONUCLARI ---")
    print(f"Toplam Kelime Sayisi: {toplam_kelime}")
    print(f"Toplam Karakter Sayisi: {toplam_karakter}")
    print("Harf Dagilimi:")
    for harf, sayi in sorted(harf_sayilari.items()):
        print(f"'{harf}': {sayi} adet")
    print("-" * 30)