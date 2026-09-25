
baslangic = 0

print("-- 5 soruluk quiz'e hoşgeldiniz.--")

print("Kullanıcıya sorular iletildiğinde, kullanıcı a, b, c şıklarından yalnızca bir tanesini seçebilir.")
print("Her doğru cevap +15 puan, her yanlış cevap -10 puandır.")

print("\n1. Soruları gör")
print("2. Cevap anahtarını gör")
print("3. Çıkış")
print("4. Bonus soruyu görmek için")

while True:

    secim = input("Seçiminiz nedir (1/2/3/4): ")

    if secim == "1":

        print("\nSoru 1:")
        print("""Türkiye'nin başkenti neresidir:

        a: Adana
        b: Mersin
        c: Ankara""")

        cevap1 = input("Cevabınız nedir (a/b/c): ").lower()

        if cevap1 != "c":
            print("Yanlış cevap verdiniz ve -10 puan yediniz.")
            baslangic -= 10
        else:
            print("Doğru cevap! 15 puan kazandınız!")
            baslangic += 15

        print("\nSoru 2:")
        print("""5 x 6'nın cevabı nedir:

        a: 10
        b: 20
        c: 30""")

        cevap2 = input("Cevabınız nedir (a/b/c): ").lower()

        if cevap2 != "c":
            print("Yanlış cevap verdiniz ve -10 puan yediniz.")
            baslangic -= 10
        else:
            print("Doğru cevap! 15 puan kazandınız!")
            baslangic += 15

        print("\nSoru 3:")
        print("""Türkiye'de kaç bölge bulunur:

        a: 5
        b: 7
        c: 4""")

        cevap3 = input("Cevabınız nedir (a/b/c): ").lower()

        if cevap3 != "b":
            print("Yanlış cevap verdiniz ve -10 puan yediniz.")
            baslangic -= 10
        else:
            print("Doğru cevap! 15 puan kazandınız!")
            baslangic += 15

        print("\nSoru 4:")
        print("""Python'da ekrana yazı yazdırmak için hangisi kullanılır:

        a: input()
        b: print()
        c: write()""")

        cevap4 = input("Cevabınız nedir (a/b/c): ").lower()

        if cevap4 != "b":
            print("Yanlış cevap verdiniz ve -10 puan yediniz.")
            baslangic -= 10
        else:
            print("Doğru cevap! 15 puan kazandınız!")
            baslangic += 15

        print("\nSoru 5:")
        print("""10 / 2 işleminin sonucu kaçtır:

        a: 5
        b: 2
        c: 10""")

        cevap5 = input("Cevabınız nedir (a/b/c): ").lower()

        if cevap5 != "a":
            print("Yanlış cevap verdiniz ve -10 puan yediniz.")
            baslangic -= 10
        else:
            print("Doğru cevap! 15 puan kazandınız!")
            baslangic += 15

        print(f"\n--- Toplam puanınız: {baslangic} ---")

    elif secim == "2":

        print(""" 
1: Ankara
2: 30
3: 7
4: print()
5: 5
""")

    elif secim == "3":

        print("Çıkış yapılıyor.")
        break

    elif secim == "4":

        print("Bonus sorusu 30 puandır, başarılar!")

        print("""Bonus soru: Suyun formülünde toplam kaç element bulunur?

        a: 3
        b: 2
        c: 4""")

        bonus_cevap = input("Cevabınız nedir (a/b/c): ").lower()

        if bonus_cevap != "b":
            print("Yanlış bildiniz, -10 puan yazıldı.")
            baslangic -= 10
        else:
            print("Doğru cevap verdiniz, 30 puan kazandınız!")
            baslangic += 30

        print(f"\n--- Bonus sorusu ile quiz sonucundaki puanınız: {baslangic} ---")

    else:
        print("Geçersiz seçim yaptınız. Lütfen 1, 2, 3 veya 4 giriniz.")




        
