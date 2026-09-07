from abc import ABC, abstractmethod


class BankaHesabi(ABC):

    def __init__(self, hesap_no, hesap_sahibi, bakiye=0.0):
        self.hesap_no = hesap_no
        self.hesap_sahibi = hesap_sahibi
        self.bakiye = bakiye

    @abstractmethod
    def para_cek(self, miktar):
        pass


class VadesizHesap(BankaHesabi):

    def __init__(
        self, hesap_no, hesap_sahibi, bakiye=0.0, eksi_bakiye_limiti=1000.0
    ):
        super().__init__(hesap_no, hesap_sahibi, bakiye)
        self.eksi_bakiye_limiti = eksi_bakiye_limiti

    def para_cek(self, miktar):
        if miktar <= (self.bakiye + self.eksi_bakiye_limiti):
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Güncel Bakiye: {self.bakiye} TL")
            return True
        else:
            print("Yetersiz bakiye.")
            return False


class VadeliHesap(BankaHesabi):

    def __init__(self, hesap_no, hesap_sahibi, bakiye=0.0, faiz_orani=0.15):
        super().__init__(hesap_no, hesap_sahibi, bakiye)
        self.faiz_orani = faiz_orani

    def para_cek(self, miktar):
        if miktar <= self.bakiye:
            self.bakiye -= miktar
            print(
                f"Vadeden önce para çekildiği için faiz iptal edildi. {miktar} TL çekildi."
            )
            return True
        else:
            print("Yetersiz bakiye.")
            return False

    def faiz_getirisi_hesapla(self):
        return self.bakiye * self.faiz_orani


# Test Alanı
if __name__ == "__main__":
    h1 = VadesizHesap("TR101", "Ahmet Yılmaz", bakiye=500)
    h2 = VadeliHesap("TR102", "Ayşe Kaya", bakiye=5000)

    h1.para_cek(800)  # Eksi bakiyeden düşer
    h2.para_cek(1000)  # Vadeli hesaptan çeker