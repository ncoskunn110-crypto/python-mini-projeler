from abc import ABC, abstractmethod

class Karakter(ABC):

    def __init__(self, isim, can, saldiri_gucu):
        self.isim = isim
        self.can = can
        self.saldiri_gucu = int(saldiri_gucu)
        self.envanter = []

    def __str__(self):
        return (
            f"{self.isim} - can: {self.can} | saldırı gücü: {self.saldiri_gucu}"
        )

    def __len__(self):
        return len(self.envanter)

    def __eq__(self, diger):
        if isinstance(diger, Karakter):
            return self.can == diger.can
        return False

    @abstractmethod
    def vurus_yap(self, hedef):
        pass

class Savasci(Karakter):
    def vurus_yap(self, hedef):
        damage = self.saldiri_gucu
        hedef.can -= damage
        print(f" {self.isim} {hedef.isim} adlı karaktere {damage} hasar verdi")

class Buyucu(Karakter):
    def __init__(self, isim, can, saldiri_gucu, mana):
        super().__init__(isim, can, saldiri_gucu)
        self.mana = int(mana)


    def vurus_yap(self, hedef):
        if self.mana >= 10:
            damage = self.saldiri_gucu * 2
            self.mana -= 10
            hedef.can -= damage
            print(
                f" {self.isim} BÜYÜ FIRLATTI! {hedef.isim} karaktere {damage} kritik hasar verdi! (Kalan Mana: {self.mana})"
            )

        else:
            damage = self.saldiri_gucu
            hedef.can -= damage
            print(
                f" {self.isim} manası bittiği için asa ile vurdu. {damage} hasar verdi."
            )

if __name__ == "__main__":
    savasci = Savasci("Barbar", can=100, saldiri_gucu=15)
    buyucu = Buyucu("Gandalf", can=70, saldiri_gucu=12, mana=20)

    savasci.envanter.extend(["Kılıç", "Kalkan", "İksir"])

    print(savasci)  # __str__ çalışır
    print(f"Savaşçının çantasındaki eşya sayısı: {len(savasci)}") 

    buyucu.vurus_yap(savasci)
    savasci.vurus_yap(buyucu)

    print(f"Canları eşit mi?: {savasci == buyucu}")