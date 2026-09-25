import random

print("Sayı tahmin oyununa hoş geldin!")
print("1 ile 100 arası bir sayı tahmin edeceksin.")

while True:

    gizli_sayi = random.randint(1, 100)
    can = 5
    deneme = 0

    while can > 0:

        try:
            tahmin = int(input("Tahminin nedir?: "))
        except ValueError:
            print("Tam sayı giriniz.")
            continue

        deneme += 1

        if tahmin < gizli_sayi:
            print("Daha yüksek söyle.")
            can -= 1

        elif tahmin > gizli_sayi:
            print("Daha küçük söyle.")
            can -= 1

        else:
            print(f"Tebrikler! {deneme}. denemede doğru bildin!")
            break

    if can == 0:
        print(f"Hakkın bitti. Gizli sayı {gizli_sayi} idi.")
        break

    tekrar = input("Tekrar oynamak ister misin? (e/h): ").lower()

    if tekrar != "e":
        print("Oyun kapatılıyor...")
        break