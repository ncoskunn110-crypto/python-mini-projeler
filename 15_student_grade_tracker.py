from datetime import datetime
import math
import json
import os

def harf_notu_hesapla(ortalama):
    """ortalamaya göre harf notunu belirler."""
    try:
        if ortalama >= 85:
            return "AA"
        elif ortalama >= 70:
            return "BB" 
        elif ortalama >= 50:
            return "CC"
        else:
            return "FF" 

    except Exception as e: 
        print(f"hesaplama hatası: {e} ")
        return "bilinmiyor"

def ogrenci_ozeti_olustur(ad, *notlar, **detaylar):
    """öğrencinin notlarını *args ek bilgileri **kwargs düzenler."""
    print(f"\n---{ad.upper()} için detaylı özet")

    if notlar:
        ortalama = sum(notlar) / len(notlar)
        yuvarlanmis_ort = math.floor(ortalama)
        harf = harf_notu_hesapla(yuvarlanmis_ort)

        print(f" girilen notlar: {notlar}")
        print(f"ortalama: {yuvarlanmis_ort} ({harf})")
    else:
        print("hiç not girilmedi.")

    if detaylar:
        print("ek bilgler:")
    for key, value in detaylar.items():
        print(f" - {key.capatalize()}: {value} ")

    DOSYA_ADI = ogrenci_kayitlari(json)

def kayitlari_oku():
        """json dosyasından mevcut kayıtları okur, try-except ile güvenli bir yöntem."""
        if not os.path.exists(DOSYA_ADI):
            return []

        try:
            with open(DOSYA_ADI, "r", encoding= "utf-8" ) as dosya:
                return json.load(dosya)
        except JSONDecodeError:
            print("uyarı: kayıt listesi bozuk veya boş. yeni liste oluşturuluyor.")
            return []
        except Exception as e:
            print(f"dosya okunurken bi hata oluştu: {e}")
            return []
def ogrenci_kaydet(ogrenci_verisi):
        """yeni öğrenci verisini JSON'a ekler."""
        kayitlar = kayitlari_oku()
        kayitlar.append(ogrenci_verisi)

        try:
            with open(DOSYA_ADI, "w", encoding="utf-8" ) as dosya:
                json.dump(kayitlar, dosya, ensure_ascii=False, indent=4)
            print("başarıyla eklendi.")
        except Exception as e:
            print(f"kayıt yazılamadı: {e}")

def ana_menu():
    while True:
        print("\n---öğrenci not takip sistemi---")
        print("1. yeni öğrenci ekle ve hesapla.")
        print("2. kayıtlı öğrencileri listele.")
        print("3. çıkış")

        secim = input("seçiminiz(1/2/3):")

        if secim == "1":
            ad = input("öğrencinin adı:")
            soyad = input("öğrencinin soy adı:")

            try:
                vize = float(input("vize notu:"))
                final = float(input("final notu:"))
            except  ValueError:
                print("hata lütfen geçerli bi sayı giriniz:")
                continue

            ogrenci_ozeti_olustur(f"{ad} {soyad}", vize, final, okul="teknoloji üniversitesi", sinif="2")

            ortalama = (vize + final) / 2
            harf = harf_notu_hesapla(ortalama)
            islem_tarihi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            veri = {
                "ad_soyad" : f"{ad} {soyad}",
                "vize": vize,
                "final": final,
                "ortalama": ortalama,
                "harf_notu": harf
                "tarih": islem_tarihi,

            }    

            ogrenci_kaydet(veri)

        elif secim == "2":
            kayitlar = kayitlari_oku()
            if not kayitlar:
                print("n/henüz kayıt oluşturulmadı.")
            else:
                print("/ngeçmiş kayıtlar")

                for i, k in enumerate(kayitlar, 1):
                    print(
                        f"{i}. {k['ad_soyad']} | Ortalama: {k['ortalama']} | Harf:"
                        f" {k['harf_notu']} | Tarih: {k['tarih']}")

        elif secim =="3":
            print("programdan çıkılıyor,görüşmek üzere!")
            break                
        else:
            print("lütfen geçerli komut giriniz.(1,2,3)")

if __name__ = "__main__":
    ana_menu()            







