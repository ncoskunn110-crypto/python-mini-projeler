arsiv = [
    {"isim": "inception", "tur": "bilim kurgu", "puan": 9},
    {"isim": "the matrix", "tur": "bilim kurgu", "puan": 9},
    {"isim": "babam ve oglum", "tur": "dram", "puan": 8}
]

import random

print("\n---kişisel medya arşivi---")

while True:
    print("\n1. arşivi incele")
    print("2. yeni medya (dizi/film) ekle")
    print("3. türe göre filtrele")
    print("4. bugun ne izlesem? (rastgele seç)")
    print("5. çıkış")

    secim = input("seçiminiz ( 1/2/3/4/5):")

    if secim == "1":
        print("\n---tüm arşiv---")
        if len(arsiv) == 0:
            print("arşiviniz henüz boş")
        else:
            for sira,medya in enumerate(arsiv,1):
                print(f"{sira}. {medya['isim']} | Tür: {medya['tur']} | Puan: {medya['puan']}/10")

    elif secim == "2":
        isim = input("eserin adı: ")
        tur = input("türü (örn: bilim kurgu,dram, komedi):").lower()

        try:
            puan = int(input("puanın 1-10 arası: "))
        except ValueError:
            print("puan sayı olmalıdır")
            continue

        yeni_medya = {"isim": isim, "tur": tur, "puan": puan} 
        arsiv.append(yeni_medya)
        print(f"'{isim}' başarıyla eklendi")

    elif secim =="3":
        aranan_tur = input("hangi türü görmek istiyorsun?: ").lower()
        bulunanlar = []

        for medya in arsiv:
            if medya ["tur"] == aranan_tur:
                bulunanlar.append(medya)

        print(f"\n--- '{aranan_tur.upper()}' TÜRÜNDEKİLER ---")
        if len(bulunanlar) == 0:
            print("bu türde kayıtlı eser bulunamadı.")
        else:
            for medya in bulunanlar:
                print(f"- {medya['isim']} (Puan: {medya['puan']})")

    elif secim == "4":
        if len(arsiv) == 0:
            print("arşivde rastgele seçilecek eser yok")
        else:
            secilen = random.choice(arsiv)
            print(f"\nSenin için seçtiğim film/kitap: **{secilen['isim']}** (Tür: {secilen['tur']}, Puan: {secilen['puan']})")


    elif secim == "5":
        print("arsiv kapatılıyor.")
        break
    else:
        ("geçersiz seçim,tekrar dene.")











