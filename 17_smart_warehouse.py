from datetime import datetime
import json
import math
import os

DOSYA_ADI = "warehouse_inventory.json"

def koli_hesapla(toplam_urun, koli_kapasitesi):
    try:
        if koli_kapasitesi <= 0:
            return 0, 0
            
        gerekli_koli = math.ceil(toplam_urun / koli_kapasitesi)
        tam_koli= math.floor(toplam_urun / koli_kapasitesi)

        return gerekli_koli, tam_koli
    except Exception as e:
        print(f"koli hesaplama hatası: {e} ")
        return 0, 0    

def urun_detaylarini_isle(urun_adi, *fiyatlar, **ozellikler):
    print(f"\n---ürün analizi: {urun_adi.upper()}---")

    ortalama_fiyat = 0
    if fiyatlar:
        ortalama_fiyat = sum(fiyatlar) / len(fiyatlar)
        print(f"geçmiş fiyatlar: {fiyatlar}") 
        print(f"ortalama piyasa fiyat: {ortalama_fiyat:.2f} TL")
    else:
        print("fiyat bilgisi girilmedi.")

    if ozellikler:
        print("ürün özellikleri:")
        for anahtar, deger in ozellikler.items():
            print(f" - {anahtar.capitalize()} : {deger}")

    return ortalama_fiyat

def veriler_oku():
    if not os.path.exists(DOSYA_ADI):
        return[]
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except json.JSONDecodeError:
        print("veri deposu bozuk yada boş.")
        return []
    except Exception as e:
        print(f"kayıt hatası: {e}")   

def veriyi_kaydet(yeni_urun):
  envanter = veriler_oku()
  envanter.append(yeni_urun)
  try:
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
      json.dump(envanter, dosya, ensure_ascii=False, indent=4)
    print("ürün başarıyla depoya kaydedildi.")
  except Exception as e:
    print(f"kaydetme hatası: {e}") 


def depo_yonetim_sistemi():
    while True:
        print("\n---akıllı depo yönetim sistemi---")
        print("1. depoya yeni ürün ekle.")
        print("2. depodaki ürünleri listele.")
        print("3. çıkış.")

        secim = input("seçiminiz (1/2/3):")
         
        if secim == "1":
            try:
                ad = input("ürünün adı:")
                adet =int(input("stoktaki toplam ürün adedi:"))
                koli_kapasite = int(input("bir koli kaç ürün alıyor:"))
                fiyat_girdisi = input(
                    "ürünün farklı tedarikçi fiyatlarını boşluk bırakarak yazınız:"
                )

                fiyat_listesi =  [float(f) for f in fiyat_girdisi.split()]

            except ValueError:
                print("hata. lütfen sayısal değerleri doğru formatta giriniz.")    
                continue

            ortalama = urun_detaylarini_isle(
                ad, *fiyat_listesi, kategori = "genel/elektronik", durum="sifir"
            )

            gerekli_koli, tam_koli = koli_hesapla(adet, koli_kapasite)
            print(f"depolama durumu: {adet} ürün için {gerekli_koli} koli gerekiyor.")

            zaman =datetime.now().strftime("%Y-%m-%d %H:%M")
            urun_paketi = {
                "urun_adi": ad,
                "adet": adet,
                "ortalama_fiyat": ortalama,
                "gerekli_koli": gerekli_koli,
                "kayit_tarihi": zaman,
            }

            veriyi_kaydet(urun_paketi)

        elif secim == "2":
            envanter = veriler_oku()
            if not envanter:
                print("\nDepo şu an tamamen boş.")
            else:
                print("\n--- DEPO ENVANTERİ ---")
                for sira, urun in enumerate(envanter, 1):
                    print(
                        f"{sira}. Ürün: {urun['urun_adi']} | Adet: {urun['adet']} | "
                        f"Ort. Fiyat: {urun['ortalama_fiyat']:.2f}TL | "
                        f"Gerekli Koli: {urun['gerekli_koli']} | Tarih: {urun['kayit_tarihi']}"
                    )

        elif secim == "3":
            print("depo sistemi kapatılıyor. görüşürüz.")
            break
        else:
            print("yanlış seçim tekrar deneyiniz.")    

if __name__ == "__main__":
    depo_yonetim_sistemi()