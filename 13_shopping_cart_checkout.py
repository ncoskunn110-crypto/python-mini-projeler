def urun_fiyati_al():
    try:
        return float(input("ürün fiyatı girin:"))
    except ValueError:
        return 0.0

def indirim_hesapla(toplam_tutar):
    if toplam_tutar > 500:
        print("500 tl üzeri alışverişte %10 indirim uygulandı.")
        return toplam_tutar * 0.90
    return toplam_tutar

def kargo_ekle(tutar):
    if tutar < 300 and tutar > 0:
        print("300 tl olduğu için 50TL kargo ücreti eklendi.")
        return tutar + 50
    print("kargo bedava.")
    return tutar

sepet_toplami = 0
print("---sepet ve kasa sistemi---")

while True:
    komut = input("ürün eklemek ister misin? (e/h):").lower()
    if komut != 'e':
        break

    fiyat = urun_fiyati_al()
    sepet_toplami += fiyat
    print(f"ara toplamı: {sepet_toplami}:")

if sepet_toplami > 0:
    indirimli_tutar = indirim_hesapla(sepet_toplami)
    son_tutar = kargo_ekle(indirimli_tutar)
    print(f"\nödemeniz gereken son tutar: {son_tutar:.2f} TL")
else:
    print("sepetiniz boş")








