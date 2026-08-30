from datetime import datetime
import json
import math
import os

DOSYA_ADI = "budget_records.json"

def butce_analizi_yap(gelir, toplam_gider):
    try:
        fark = gelir - toplam_gider
        mutlak_fark = math.fabs(fark)

        sapma_koku =math.sqrt(mutlak_fark) if mutlak_fark > 0 else 0.0

        return fark, mutlak_fark, sapma_koku
    except Exception as e:   
        print(f"matematiksel hesaplama hatası: {e}")
        return 0, 0, 0

def harcama_ozeti_olustur(kullanici, *harcamalar, **ek_bilgiler):
    print(f"\n--- {kullanici.upper()} için harcama raporu---")

    if harcamalar:
        toplam_gider = sum(harcamalar)
        print(f"girilen harcama kalemleri: {harcamalar}")
        print(f"toplam gider: {toplam_gider} TL")

    else:
        toplam_gider = 0
        print("bu islemde henuz harcama kalemi girilmedi.")

    if ek_bilgiler:        
        print("işlem detayları:")
        for anahtar, deger in ek_bilgiler.items():
            print(f" - {anahtar.capitalize()}: {deger} ")

    return toplam_gider

def kayitlari_yukle():
    if not os.path.exists(DOSYA_ADI):
        return []
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except json.JSONDecodeError: 
        print("bütçe dosyası bozulmuş,yeniden oluşturuluyor.")
        return []
    except Exception as e:
        print(f"dosya okuma hatası: {e}")
        return[]

def harcama_kaydet(veri):
    kayitlar = kayitlari_yukle()
    kayitlar.append(veri)
    try:
        with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
            json.dump(kayitlar, dosya, ensure_ascii=False, indent= 4)
        print("harcama basarıyla butceye islendi.")
    except  Exception as e:
        print(f"kayıt kaydedilemedi: {e}")

def butce_asistani():
    while True:
        print("\n---kişisel bütçe asistanı---") 
        print("1. yeni gelir ve harcama girişi yap")
        print("2. tüm bütçe geçmişini görüntüle") 
        print("3. çıkış")

        secim = input("seçiminiz (1/2/3):") 

        if secim == "1":
            isim = input("adınız?:")

            try:
                gelir = float(input("aylık / günlük geliriniz:"))
                girdi_harcamalar = input("harcama kalemlerinzi boşluk bırakarak yazınız. (örn: 150 45.5):")

                harcama_listesi = [float(x) for x in girdi_harcamalar.split()]  
            except ValueError:
                print("hata! lütfen sayısal değerler giriniz.")
                continue

            toplam_gider = harcama_ozeti_olustur(
                isim,
                *harcama_listesi,
                odeme_turu = "kredi kartı/ nakit",
                para_birimi = "TL",
            )

            fark, mutlak_fark, sapma = butce_analizi_yap(gelir, toplam_gider)

            if fark >= 0:
                durum = f"karda/artıdasınız kalan: {fark} TL"
            else:
                durum = f" bütçe açığı var. eksi: {mutlak_fark} TL"

            print(f"durum analizi: {durum}")
            print(f"bütçe sapma katsayısı: (karekök) {sapma:.2f}")

            zaman_damgasi = datetime.now().strftime("%d.%m.%Y - %H:%M")
            veri_paketi= {
                "kullanici": isim,
                "gelir": gelir,
                "toplam_gider": toplam_gider,
                "net_durum": fark,
                "tarih": zaman_damgasi,

            }

            harcama_kaydet(veri_paketi)

        elif secim == "2": 
            kayitlar = kayitlari_yukle()
            if not kayitlar:
                print("\nhenüz kayıtlı bir işlem yok")
            else:
                print("\n---bütçe geçmişi---")
                for sira, k in enumerate(kayitlar,1):
                    print(
                         f"{sira}. {k['kullanici']} | Gelir: {k['gelir']}TL | Gider:"
                         f" {k['toplam_gider']}TL | Net: {k['net_durum']}TL | Tarih:"
                         f" {k['tarih']}"
                    )

        elif secim == "3":
            print("bütçe asistanı kapatılıyor. görüşmek üzere.") 
            break
        else:
            print("geçersiz seçim,yeniden deneyin")

if __name__ == "__main__":
    butce_asistani()











