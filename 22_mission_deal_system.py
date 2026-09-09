from abc import ABC, abstractmethod
from datetime import datetime
import json
import time
import os

def log_ve_sure_olc(func):
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        sonuc = func(*args, **kwargs)
        bitis = time.time()
        gecen_sure = (bitis - baslangic) * 1000
        print(f"⏱️ [LOG] '{func.__name__}' metodu {gecen_sure:.2f} ms'de çalıştı.")
        return sonuc
    return wrapper

class GorevBulunamadiHatasi(Exception):
    pass

class YetkisizİslemHatasi(Exception):
    pass

class Gorev(ABC):
    def __init__(self, gorev_id, baslik, *etiketler, **detaylar):
        self.gorev_id = gorev_id
        self.baslik = baslik
        self.tamamlandi_mi = False
        self.olusturulma_tarihi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.etiketler = list(etiketler)
        self.detaylar = detaylar

    @abstractmethod
    def aciliyet_skoru_ayarla(self):
        pass

    def __str__(self):
        durum = "Tamamlandı" if self.tamamlandi_mi else "Devam Ediyor"
        etiket_metni = (
            ", ".join(f"#{e}" for e in self.etiketler)
            if self.etiketler
            else "Etiket Yok"
        )
        return f"[{self.gorev_id}] {self.baslik} | Durum: {durum} | Etiketler: {etiket_metni}"

    def to_dict(self):
        return {
            "gorev_id": self.gorev_id,
            "baslik": self.baslik,
            "tamamlandi_mi": self.tamamlandi_mi,
            "olusturma_tarihi": self.olusturulma_tarihi,
            "etiketler": self.etiketler,
            "detaylar": self.detaylar,
            "tip": self.__class__.__name__,
        }

class YazilimGorevi(Gorev):
    def __init__(self, gorev_id, baslik, modul_adi, *etiketler, **detaylar):
        super().__init__(gorev_id, baslik, *etiketler, **detaylar)
        self.modul_adi = modul_adi

    def aciliyet_skoru_ayarla(self):
        skor = 50
        if "KRİTİK" in [e.upper() for e in self.etiketler]:
            skor += 40
        return skor

class TasarimGorevi(Gorev):
    def __init__(self, gorev_id, baslik, revizyon_sayisi, *etiketler, **detaylar):
        super().__init__(gorev_id, baslik, *etiketler, **detaylar)
        self.revizyon_sayisi = int(revizyon_sayisi)

    def aciliyet_skoru_ayarla(self):
        return 30 + (self.revizyon_sayisi * 10)

class ProjeYoneticisi:
    def __init__(self, proje_adi, dosya_adi="gorevler.json"):
        self.proje_adi = proje_adi
        self.dosya_adi = dosya_adi
        self.gorevler = []
        self._verileri_yukle()

    def _verileri_yukle(self):
        if not os.path.exists(self.dosya_adi):
            return

        try:
            with open(self.dosya_adi, "r", encoding="utf-8") as f:
                ham_veriler = json.load(f)

                for g in ham_veriler:
                    if g["tip"] == "YazilimGorevi":
                        obj = YazilimGorevi(
                            g["gorev_id"],
                            g["baslik"],
                            g["detaylar"].get("modul", "Genel"),
                            *g["etiketler"],
                            **g["detaylar"],
                        )
                    else:
                        obj = TasarimGorevi(
                            g["gorev_id"],
                            g["baslik"],
                            g["detaylar"].get("revizyon", 1),
                            *g["etiketler"],
                            **g["detaylar"],
                        )
                    obj.tamamlandi_mi = g["tamamlandi_mi"]
                    self.gorevler.append(obj)
        except Exception as e:
            print(f"Veri yükleme hatası: {e}")

    @log_ve_sure_olc
    def verileri_kaydet(self):
        try:
            veri_listesi = [g.to_dict() for g in self.gorevler]
            with open(self.dosya_adi, "w", encoding="utf-8") as f:
                json.dump(veri_listesi, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Veri kaydetme hatası: {e}")

    @log_ve_sure_olc
    def gorev_ekle(self, gorev_nesnesi):
        self.gorevler.append(gorev_nesnesi)
        self.verileri_kaydet()
        print(f"Görev Eklendi: {gorev_nesnesi.baslik}")

    def gorev_tamamla(self, gorev_id):
        gorev = next((g for g in self.gorevler if g.gorev_id == gorev_id), None)

        if not gorev:
            raise GorevBulunamadiHatasi(f"Görev ID {gorev_id} bulunamadı.")

        gorev.tamamlandi_mi = True
        self.verileri_kaydet()
        print(f"Görev tamamlandı olarak işaretlendi: {gorev.baslik}")

    def gorevleri_raporla(self, sadece_tamamlanmayanlar=False):
        if not self.gorevler:
            print("Projede henüz görev yok.")
            return

        if sadece_tamamlanmayanlar:
            listelenecekler = list(
                filter(lambda g: not g.tamamlandi_mi, self.gorevler)
            )
        else:
            listelenecekler = self.gorevler

        print("\n" + "=" * 60)
        print(
            f"📋 PROJE GÖREV RAPORU: {self.proje_adi.upper()} (Toplam: {len(self.gorevler)} Görev)"
        )
        print("=" * 60)

        for sira, g in enumerate(listelenecekler, 1):
            skor = g.aciliyet_skoru_ayarla()
            detay_str = ", ".join(f"{k}: {v}" for k, v in g.detaylar.items())
            print(
                f"{sira}. {g} | Aciliyet Skoru: {skor} | Detaylar: [{detay_str}]"
            )

if __name__ == "__main__":
    yonetici = ProjeYoneticisi("E-Ticaret Dönüşüm Projesi")

    # *args (etiketler) ve **kwargs (detaylar) ile esnek görev oluşturma
    g1 = YazilimGorevi(
        "TSK-101",
        "Ödeme Arayüzü Entegrasyonu",
        "Ödeme Modülü",
        "KRİTİK",
        "Backend",
        "Acil",
        geliştirici="Ahmet",
        tahmini_saat=8,
    )

    g2 = TasarimGorevi(
        "TSK-102",
        "Ana Sayfa Banner Tasarımı",
        3,
        "UI/UX",
        "Grafik",
        tasarimci="Ayşe",
        format="Figma",
    )

    # Görevleri ekleme
    yonetici.gorev_ekle(g1)
    yonetici.gorev_ekle(g2)

    # Görev tamamlama testi
    try:
        yonetici.gorev_tamamla("TSK-101")
    except GorevBulunamadiHatasi as e:
        print(e)

    # Raporlama
    yonetici.gorevleri_raporla(sadece_tamamlanmayanlar=False)