import time
import datetime

print("\n---pomodoro odaklanma asistanı---")
print("1. standart odaklanma başlat (25 dakika çalışma)")
print("2. kısa mola başlat (5 dakika dinlenme)")
print("3. özel süre gir")
print("4. çıkış")

while True:
    secim = input("\nseçiminiz (1/2/3/4):")

    saniye = 0
    
    if secim == "1":
        saniye = 25 * 60
        print("25 dakikalık odaklanma başladı, kolay gelsin")
    elif secim == "2":
        saniye = 5 * 60
        print("5 dakikalık kısa mola başladı, dinlenin")
    elif secim == "3":
        try:
            dakika = int(input("kaç dakika odaklanmak istiyorsunuz?:"))
            saniye = dakika * 60
        except ValueError:
            print("lütfen geçerli bir sayı girin")
            continue
    elif secim == "4":
        print("pomodoro asistanı  kapatılıyor,  görüşmek üzere")
        break
    else:
        print("geçersiz seçim tekrar dene")
        continue
    print("\nsüreniz başladı, (iptal etmek içim Ctrl + C yapabiirsiniz.)")

    try:
        while saniye > 0:
            dakika_kalan = saniye // 60
            saniye_kalan = saniye % 60 

            print(f"\rKalan Süre: {dakika_kalan:02d}:{saniye_kalan:02d}", end="")
            time.sleep(1)
            saniye -= 1
        print("\n\nsüre bitti, harika bir iş çıkardın")

        simdi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("pomodoro_gecmis.txt", "a" , encoding="utf-8") as dosya:
            dosya.write(f"tamamlanan seans: {simdi} \n")

    except KeyboardInterrupt:
        print("\n\nsüre yarıda kesildi")
        





