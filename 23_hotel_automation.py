from abc import ABC, abstractmethod
from datetime import datetime
import json
import math
import os
import time

def islem_logla(func):
    def wrapper(*args, **kwargs):
        baslangic= time.time()
        sonuc = func(*args, **kwargs)
        sure = (time.time() - baslangic) * 1000
        zaman = datetime.now().strftime("%H:%M:%S")
        print(
            f"⏱️ [{zaman}] '{func.__name__}' metodu başarıyla çalıştı ({sure:.2f} ms)."
        )
        return sonuc

    return wrapper

class ODA_DOKU_HATASI(Exception):
    pass

class BAKIYE_YETERSIZ_HATASI(Exception):
    pass

class Oda(ABC):
    def __init__(self, oda_no, taban_fiyat, **ozellikler):
        self.oda_no = int(oda_no)
        self.taban_fiyat = float(taban_fiyat)
        self.dolu_mu = False
        self.ozellikler = ozellikler

    @abstractmethod
    def fiyat_hesapla(self, gece_sayisi):
        pass

    def to_dict(self):
        return{
            "oda_no": self.oda_no,
            "taban_fiyat": self.taban_fiyat,
            "dolu_mu": self.dolu_mu,
            "ozellikler": self.ozellikler,
            "tip": self.__class__.__name__,  
        }

class StandartOda(Oda):
    def fiyat_hesapla(self, gece_sayisi):
        ham_tutar = self.taban_fiyat * gece_sayisi
        if gece_sayisi >= 3:
            ham_tutar *= 0.95
            return math.ceil(ham_tutar)

class KralDairesi(Oda):

    def __init__(self, oda_no, taban_fiyat, hizmetci_servisi = True, **ozellikler ):
        super().__init__(oda_no, taban_fiyat, **ozellikler)
        self.hizmetci_servisi = hizmetci_servisi

    def fiyat_hesapla(self, gece_sayisi):
        ham_tutar = (self.taban_fiyat * 1.5) * gece_sayisi
        if self.hizmetci_servisi:
            ham_tutar += 2000.0
            return math.ceil(ham_tutar)

class OtelYonetimi:
    def __init__(self, otel_adi, dosya_adi="otel_verileri.json"):
        self.otel_adi = otel_adi
        self.dosya_adi = dosya_adi
        self.odalar = []
        self._verileri_yukle()

    def _verileri_yukle(self):
        if not os.path.exists(self.dosya_adi):
            return

        try:
            with open(self.dosya_adi, "r", encoding="utf-8") as f:
                ham_data = json.load(f)
                for item in ham_data:
                    if item["tip"] == "KralDairesi":
                        obj = KralDairesi(
                            item["oda_no"], item["taban_fiyat"], **item["ozellikler"]
                        )
                    else:
                        obj = StandartOda(
                            item["oda_no"], item["taban_fiyat"], **item["ozellikler"]
                        )
                    obj.dolu_mu = item["dolu_mu"]
                    self.odalar.append(obj)
        except Exception as e:
            print(f"⚠️ Dosya yükleme hatası: {e}")

    @islem_logla
    def verileri_kaydet(self):
        try:
            dict_list = [o.to_dict() for o in self.odalar]
            with open(self.dosya_adi, "w", encoding="utf-8") as f:
                json.dump(dict_list, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f" Kayıt hatası: {e}")

    def toplu_oda_ekle(self, *oda_nesneleri):
        for oda in oda_nesneleri:
            if any(o.oda_no == oda.oda_no for o in self.odalar):
                print(f"⚠️ {oda.oda_no} numaralı oda zaten mevcut, atlanıyor.")
                continue
            self.odalar.append(oda)
        self.verileri_kaydet()


    def oda_rezerve_et(self, oda_no, gece_sayisi):

        oda = next((o for o in self.odalar if o.oda_no == oda_no), None)

        if not oda:
            print(f"❌ {oda_no} numaralı oda sistemde yok!")
            return

        if oda.dolu_mu:
            raise ODA_DOLU_HATASI(
                f"❌ {oda_no} numaralı oda şu an dolu! Rezervasyon yapılamaz."
            )

        toplam_tutar = oda.fiyat_hesapla(gece_sayisi)
        oda.dolu_mu = True
        self.verileri_kaydet()

        print("\n" + "=" * 40)
        print(f"🏨 REZERVASYON ONAYLANDI ({self.otel_adi})")
        print(f"• Oda No     : {oda.oda_no}")
        print(f"• Konaklama : {gece_sayisi} Gece")
        print(f"• Toplam    : {toplam_tutar:.2f} TL")
        print("=" * 40)

    
    def bos_odalari_raporla(self, max_butce= None):
        if not self.odalar:
            print("otelde tanımlı oda bulunamadı.")
            return

        boslar = list(filter(lambda o: not o.dolu_mu, self.odalar))

        if max_butce:
            boslar = list(filter(lambda o: o.taban_fiyat <= max_butce, boslar))

        print("\n" + "-" * 50)
        print(f"🔑 UYGUN (BOŞ) ODALAR LİSTESİ (Toplam: {len(boslar)})")
        print("-" * 50)

        # ENUMERATE KULLANIMI
        for sira, o in enumerate(boslar, 1):
            # Dict comprehension / string join
            ozellik_metni = ", ".join(f"{k}: {v}" for k, v in o.ozellikler.items())
            print(
                f"{sira}. Oda No: {o.oda_no} | Taban Fiyat: {o.taban_fiyat} TL | [{ozellik_metni}]"
            )

if __name__ == "__main__":
    otel = OtelYonetimi("Titanik Lüks Resort")

    # **kwargs ile esnek oda nitelikleri tanımlama
    o1 = StandartOda(101, 1500.0, manzara="Deniz", yatak="Çift Kişilik")
    o2 = StandartOda(102, 1200.0, manzara="Kara", yatak="Tek Kişilik")
    o3 = KralDairesi(501, 5000.0, hizmetci_servisi=True, jakuzi=True, teras=True)

    # *args ile toplu fırlatma
    otel.toplu_oda_ekle(o1, o2, o3)

    # Boş odaları filtreli raporlama (Lambda & Filter)
    otel.bos_odalari_raporla(max_butce=2000)

    # Rezervasyon Denemeleri (Guard Clause & Custom Exception)
    try:
        otel.oda_rezerve_et(101, 3)
        # otel.oda_rezerve_et(101, 2) # İkinci kez çağrılırsa ODA_DOLU_HATASI patlar!
    except ODA_DOLU_HATASI as e:
        print(e)           