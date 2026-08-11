import random

en_iyi_skor = None

print("\n---sayı tahmin oyununa hoşgeldin---")
print("1 ile 100 arasında bir sayı tuttum, bakalım tahmin edebilecek misin?")

while True:
    gizli_sayi = random.randint(1, 100)
    deneme_sayisi = 0

    print("\nyeni oyun başlıyor, bir sayı tahmin et (1-100)")

    while True:
        try:
             tahmin = int(input("tahmininzi giriniz:"))
        except ValueError:
            print("lütfen sadece tam sayı giriniz")
            continue

        deneme_sayisi += 1
        if tahmin < gizli_sayi:
            print("daha büyük bir sayı söylemen gerekiyor")
        elif tahmin > gizli_sayi:
            print("daha küçük bir sayı söylemen gerekiyor")
        else:
            print(f"tebrikler {deneme_sayisi} denemede doğru tahmin ettiniz!")

            if en_iyi_skor is None or deneme_sayisi < en_iyi_skor:
                en_iyi_skor = deneme_sayisi
                print(f"yeni en iyi skorunuz: {en_iyi_skor} deneme")
            else:
                 print(f"suanki en iyi skorunuz: {en_iyi_skor} deneme") 
            break

    tekrar = input("tekrar oynamak ister misiniz? (e/h):")       
    if tekrar != "e":
        print("oyun kapatılıyor, en iyi skorunuz: {} deneme".format(en_iyi_skor))
        break
         
