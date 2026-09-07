from abc import ABC, abstractmethod
from datetime import datetime
import json
import math
import os

class VeriFormatiHatasi(Exception):
    pass

class SatisKayit(ABC):
    def __init__(self, islem_id, birim_fiyat, adet, **ek_bilgiler):
        self.islem_id = islem_id
        self.birim_fiyat = float(birim_fiyat)
        self.adet = int(adet)
        self.ek_bilgiler = ek_bilgiler

    @abstractmethod
    def net_tutar_hesapla(self):
        pass

    def to_dict(self):
        return {
            "islem_id": self.islem_id,
            "birim_fiyat": self.birim_fiyat,
            "adet": self.adet,
            "ek_bilgiler": self.ek_bilgiler,
            "net_tutar": self.net_tutar_hesapla(),
        }

class PerakendeSatis(SatisKayit):

    def net_tutar_hesapla(self):
        ham_tutar = self.birim_fiyat * self.adet
        kdvli_tutar = ham_tutar * 1.20
        return math.ceil(kdvli_tutar)

class ToptanSatis(SatisKayit):
    def __init__(self, islem_id, birim_fiyat, adet, iskonto_orani=0.10, **ek ):
        super().__init__(islem_id, birim_fiyat, adet, **ek)
        self.iskonto_orani = float(iskonto_orani)

    def net_tutar_hesapla(self):
        ham_tutar = self.birim_fiyat * self.adet
        iskontolu = ham_tutar * (1 - self.iskonto_orani)
        return math.floor(iskontolu)


class RaporlamaMotoru:
    def __init__(self, dosya_adi = "satislar.json"):
        self.dosya_adi = dosya_adi
        self.satislar = []
        self._dosyadan_oku()


    def _dosyadan_oku(self):
        if not os.path.exists(self.dosya_adi):
            return

        try:
            with open(self.dosya_adi, "r", encoding= "utf-8") as f:
                ham_data = json.load(f)

                for item in ham_data:
                    ek = item.get("ek_bilgiler", {})
                    if ek.get("tip") == "toptan":
                        obj = ToptanSatis(
                            item["islem_id"],
                            item["birim_fiyat"],
                            item["adet"],
                            **ek,
                        )
                    else:
                        obj = PerakendeSatis(
                            item["islem_id"],
                            item["birim_fiyat"],
                            item["adet"],
                            **ek,
                        ) 

                    self.satislar.append(obj)
        except EXception as e:
           print(f"veri yüklenirken hata oluştu: {e}")

    def veriyi_kaydet(self):
        try:
            dict_listesi = [s.to_dict() for s in self.satislar]    
            with open(self.dosya_adi, "w", encoding="utf-8") as f:
                json.dump(dict_listesi, f, ensure_ascii=False, indent=4)   
        except Exception as e:
            print(f"kayıt hatası: {e}")


    def toplu_satis_isle(self, *satis_nesneleri):
        for satis in satis_nesneleri:
            if satis.birim_fiyat <= 0 or satis.adet <= 0:
                raise VeriFormatiHatasi(
                    f"İşlem {satis.islem_id}: Fiyat ve adet 0'dan büyük olmalıdır!"
                )

            self.satislar.append(satis)

    def istatiksel_analiz_yap(self, min_tutar = 0):
        if not self.satislar:
            print("analiz yapılacak veri bulunamadı.")
            return


        suzulmus_satislar = list(
            filter(lambda s: s.net_tutar_hesapla() >= min_tutar, self.satislar)
        )

        # 2. MAP & LAMBDA: Tüm net tutarları bir listeye çıkarma
        net_tutarlar = list(
            map(lambda s: s.net_tutar_hesapla(), suzulmus_satislar)
        )

        # MATH & İSTATİSTİK
        toplam_ciro = sum(net_tutarlar)
        ortalama_satis = (
            toplam_ciro / len(net_tutarlar) if net_tutarlar else 0
        )
        en_yuksek_satis = max(net_tutarlar) if net_tutarlar else 0

        print("\n" + "=" * 50)
        print(
            f"📈 SATIŞ VE İSTATİSTİK ANALİZİ ({datetime.now().strftime('%Y-%m-%d')})"
        )
        print("=" * 50)
        print(f"• Analiz Edilen İşlem Sayısı : {len(suzulmus_satislar)}")
        print(f"• Toplam Ciro                : {toplam_ciro:.2f} TL")
        print(f"• Ortalama İşlem Tutarı     : {ortalama_satis:.2f} TL")
        print(f"• En Yüksek Satış Tutarı     : {en_yuksek_satis:.2f} TL")
        print("-" * 50)

        
        print("\n DETAYLI İŞLEM LİSTESİ:")
        for sira, s in enumerate(suzulmus_satislar, 1):
            # Dict Comprehension ile metin hazırlığı
            detay = ", ".join(f"{k}: {v}" for k, v in s.ek_bilgiler.items())
            print(
                f" {sira}. ID: {s.islem_id} | Adet: {s.adet} | Net Tutar: {s.net_tutar_hesapla()} TL | [{detay}]"
            )


if __name__ == "__main__":
    analizor = RaporlamaMotoru()

    # **kwargs ile esnek veri gönderimi
    s1 = PerakendeSatis(
        "ST-101",
        150.0,
        2,
        kategori="Elektronik",
        sehir="İstanbul",
        tip="Perakende",
    )
    s2 = ToptanSatis(
        "ST-102",
        500.0,
        10,
        iskonto_orani=0.15,
        kategori="Gida",
        sehir="Ankara",
        tip="Toptan",
    )
    s3 = PerakendeSatis(
        "ST-103",
        40.0,
        5,
        kategori="Kirtasiye",
        sehir="Adana",
        tip="Perakende",
    )

    try:
       
        analizor.toplu_satis_isle(s1, s2, s3)
    except VeriFormatiHatasi as e:
        print(f"❌ {e}")

    
    analizor.istatiksel_analiz_yap(min_tutar=200)
