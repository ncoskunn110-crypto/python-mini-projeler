from datetime import datetime

class Kisi:
    def __init__(self, tc_no, ad_soyad, dogum_yili):
        self.tc_no = tc_no
        self.ad_soyad = ad_soyad
        self.dogum_yili = int(dogum_yili)

    @property
    def yas(self):
        """Doğum yılından otomatik yaş hesabı yapar (ReadOnly Property)."""
        mevcut_yil = datetime.now().year
        return mevcut_yil - self.dogum_yili

    def kimlik_bilgisi(self):
        return f"{self.ad_soyad} (TC: {self.tc_no}) - Yaş: {self.yas}"


class Doktor(Kisi):
    def __init__(self, tc_no, ad_soyad, dogum_yili, uzmanlik_alani):
        super().__init__(tc_no, ad_soyad, dogum_yili)
        self.uzmanlik_alani = uzmanlik_alani
        self.randevular = []

    def randevu_ekle(self, hasta, tarih_saat):
        self.randevular.append({"hasta": hasta, "tarih": tarih_saat})
        print(f"✅ Dr. {self.ad_soyad} kalenderine randevu eklendi: {hasta.ad_soyad} -> {tarih_saat}")


class Hasta(Kisi):
    def __init__(self, tc_no, ad_soyad, dogum_yili, kan_grubu):
        super().__init__(tc_no, ad_soyad, dogum_yili)
        self.kan_grubu = kan_grubu
        self.reçeteler = []

    def recete_yaz(self, ilac_adi):
        self.reçeteler.append(ilac_adi)
        print(f"💊 {self.ad_soyad} adlı hastaya ilaç tanımlandı: {ilac_adi}")


# TEST ALANI
if __name__ == "__main__":
    doktor1 = Doktor("12345678901", "Ahmet Yılmaz", 1980, "Dahiliye")
    hasta1 = Hasta("98765432109", "Ayşe Kaya", 1995, "A Rh+")

    print(doktor1.kimlik_bilgisi())
    print(hasta1.kimlik_bilgisi())

    doktor1.randevu_ekle(hasta1, "2026-03-10 14:00")
    hasta1.recete_yaz("Parasetamol")