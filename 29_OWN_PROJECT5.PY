sozluk = {
    "konser": {
        "fiyat": 190,
        "saat": "19.10",
        "süre": "60 dk",
        "şehir": "Manisa"
    },

    "opera": {
        "fiyat": 200,
        "saat": "19.20",
        "süre": "40 dk",
        "şehir": "İstanbul"
    },

    "film gecesi": {
        "fiyat": 300,
        "saat": "20.05",
        "süre": "30 dk",
        "şehir": "Adana"
    },

    "tiyatro": {
        "fiyat": 150,
        "saat": "21.00",
        "süre": "25 dk",
        "şehir": "Malatya"
    },
}

import random

butce = 700

print("\n18 eylülde yapılacak etkinliklerden hangisini seçeceksiniz?")
print("\nkatılım şartları:")
print("- 18 yaş altı hiçbir etkinliğe katılamaz.")
print("- aynı anda max 2 etkinliğe katılınabilir.")

while True:
    yas = int(input("yaşınızı giriniz:"))
    if yas < 18:
            print("katılmak için yaşınız yetmiyor.")
            break
    else:
            print("devam edebilirsiniz")
            
    while True:

            print("\n1. etkinlik ayrıntılarını görmek için")
            print("2. eklemek istediğiniz etkinlik var ise")
            print("3. etkinliğin hangi şehirde olduğu")
            print("4. hangi etkinliklere katılınırsa ödenmesi gereken miktar")
            print("5. sizin için rastgele seçim yapmamızı istiyorsanız")
            print("6. çıkış")

            secim = input("seçiminiz(1/2/3/4/5/6):")
                

            if secim == "6":
                    print("programdan çıkılıyor...")
                    break

            elif secim == "1":
                        for key in sozluk.keys():
                                print(f"- {key}")

                        tercih = input("hangisini seçmek istiyorsunuz? (Örn: konser veya tiyatro konser): ").lower()
                        secilenler = tercih.split()


                        if tercih in sozluk:
                            fiyat = sozluk[tercih]["fiyat"]
                            saat = sozluk[tercih]["saat"]
                            sure = sozluk[tercih]["süre"]
                    
                            print(f"\n--- {tercih.upper()} DETAYLARI ---")
                            print(f"Saat: {saat} | Süre: {sure} | Ücret: {fiyat}")
                            
                            onay = input("Onaylamak için 'e' bas: ").lower()
                            if onay != "e":
                                print("çıkış yapılıyor...")
                            else: 
                                print("ödemeniz tamamlandı...")
                                print("İşlem başarıyla gerçekleşti!")

                        elif len(secilenler) > 2:
                            print("Üzgünüm, aynı anda en fazla 2 etkinliğe katılabilirsiniz!")

            
                        elif len(secilenler) == 2 and secilenler[0] in sozluk and secilenler[1] in sozluk:
                            etkinlik1 = secilenler[0]
                            etkinlik2 = secilenler[1]
                            
                            fiyat1 = sozluk[etkinlik1]["fiyat"]
                            fiyat2 = sozluk[etkinlik2]["fiyat"]
                            toplam_fiyat = fiyat1 + fiyat2
                            
                            print(f"\n--- İKİLİ SEÇİM DETAYLARI ---")
                            print(f"{etkinlik1.capitalize()} ({sozluk[etkinlik1]['saat']}) ve {etkinlik2.capitalize()} ({sozluk[etkinlik2]['saat']}) seçtiniz.")
                            print(f"Ödemeniz gereken toplam miktar: {toplam_fiyat} TL")
                            
                            onay = input("Onaylamak için 'e' bas: ").lower()
                            if onay != "e":
                                print("çıkış yapılıyor...")
                            else: 
                                print("ödemeniz tamamlandı...")
                                print(f"Kalan bakiye: {700 - toplam_fiyat} TL")
            elif secim == "2":
                        adi = input("eklemek istediğiniz etkinliğin adı:")
                        ucreti = input("eklemek istediğiniz etkinliğin ücreti:")
                        saati = input("eklemek istediğiniz etkinliğin saat kaçta olduğu:")
                        suresi = input("eklemek istediğiniz etkinliğin ne kadar süreceği:")
                        sozluk[adi] = {"fiyat": ucreti, "saat": saati, "suresi": suresi}
                        print(f"'{adi}' başarıyla eklendi!")

                        karar = input("eklediğiniz etkinlikle aynı gün olan mevcut etkinliklere katılamazsınız. onaylıyor musunuz(evet/hayır):")
                        if karar != "evet":
                            print("o zaman eklemeyin")
                            break
                        else:
                            print("harika devam edebiliriz.")

            elif secim == "3":
                        sehir_adi = input("yerini bilmek istediğiniz etkinliğin adı:").lower()
                        if sehir_adi == "konser":
                            print("konser Manisa'dadır")
                        elif sehir_adi == "opera":
                            print(" opera İstanbul'dadır")
                        elif sehir_adi == "tiyatro":
                            print(" tiyatro Malatya'dadır")
                        elif sehir_adi == "film gecesi":
                            print("film gecesi Adana'dadır")
                        else:
                            print("bu etkinlik listede yok.")

                        print("-" * 30) 

           
                        kullanici_etkinlik_adi = input("Kendi eklediğiniz etkinliğin adı nedir? (Yoksa 'yok' yazın): ").lower()
            
                        if kullanici_etkinlik_adi != "yok" and kullanici_etkinlik_adi in sozluk:
                            sizin_sehir = input(f"'{kullanici_etkinlik_adi}' etkinliği hangi şehirde?: ")
                            
                            
                            sozluk[kullanici_etkinlik_adi]["sehir"] = sizin_sehir
                            print(f"'{sizin_sehir}' şehri başarıyla '{kullanici_etkinlik_adi}' etkinliğine eklendi!")
                        else:
                            print("Yeni bir etkinlik eklenmedi veya böyle bir etkinlik sözlükte bulunamadı.")
                        
                        detaylar = input("tüm etkinlikleri tekrardan görmek için 7 ye basınız:")
                        if detaylar == "7":
                            for key, deger in sozluk.items():
                                print(f"{key} ---> {deger}")
                        else:
                            print("çıkış yapılıyor...")

            elif secim == "4": 
                        fiyat = input("hangi etkinliğin fiyatını görmek istiyorsunuz?(sadece 1 etkinlik adı yazılabilir..):")
                        if fiyat == "konser":
                            print(sozluk["konser"]["fiyat"])
                        elif fiyat  == "opera":
                            print(sozluk["opera"]["fiyat"])
                        elif fiyat == "tiyatro":
                            print(sozluk["tiyaro"]["fiyat"])
                        elif fiyat == "film gecesi":
                            print(sozluk["film gecesi"]["fiyat"])
                        else:
                            print("bu isimde bir etkinlik yok.")

            elif secim == "5":
                        rastgele_secim = random.choice(list(sozluk.keys()))
                        print(f"Rastgele Seçilen: {rastgele_secim}")
                        print(f"Ücret: {sozluk[rastgele_secim]['fiyat']}")
                        print(f"Saat: {sozluk[rastgele_secim]['saat']}")
                        print(f"Süre: {sozluk[rastgele_secim]['süre']}")


                


