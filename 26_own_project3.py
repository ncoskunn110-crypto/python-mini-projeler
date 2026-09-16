import random
can = 5
deneme = 0

print("sayı tahmin oyununa hoş geldin")
print("1 ile 100 arası bir sayı tahmin edeceksin.")


while True:
    
    gizli_sayi = random.randint(1, 100)
    deneme_sayisi = 0

    while can > 0:

        try:
            tahmin = int(input("tahminin nedir?:"))
        except ValueError:
            print("tam sayı giriniz.")
            continue

        if tahmin < gizli_sayi:
            print("daha yüksek söyle")
            can -= 1
            deneme += 1

        elif tahmin > gizli_sayi:
            print("daha küçük söyle.")
            can -= 1
            deneme +=1
            
    
        else:
            print(f"tebrikler {deneme} denemede doğru bildin!")
            break


    if can == 0:
        print("hakkın bitti, oyun kapatılıyor...")
        break
            

    tekrar = input("tekrar oynamak ister misin? (e/h):")
    if tekrar != "e":
        print("oyun kapatılıyooor.")
        break