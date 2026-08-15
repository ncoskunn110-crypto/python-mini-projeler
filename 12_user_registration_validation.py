print("--- güvenli kayıt ekranı---")

while True:
    kullanici_adi = input("\nkullanıcı adı belirle (en az 3 harf):").strip()

    if len(kullanici_adi) < 3:
        print("hata! kullanici adi en az 3 harf olmalıdır. ")
        continue

    sifre = input("sifre belirle ( en az 6 karakter olmalı ve rakam içermelidir.):").strip()

    if len(sifre) < 6:
        print("hata! en az 6 karakter içermelidir.")
        continue
    rakam_var_mi = False
    for karakter in sifre:
        if karakter.isdigit():
            rakam_var_mi =  True
            break

    if not rakam_var_mi:
        print("hata: şifreniz en az 1 adet rakam içermelidir.")
        continue

    try:
        yas = int(input("yaşınızı giriniz:"))
        if yas < 18:
            print("hata: 18 yaşından küçükler kaydolamaz.")
            continue
    except ValueError:
        print("hata: yaş kısmına harf yazamazsın,yeniden dene.")
        continue

    print(f"tebrikler kaydınız başarıyla oluşturuldu.")
    print(f"kullanıcı adı: {kullanici_adi}, yaş : {yas}")

    kayit_et = input("\nbaşka bir kayıt yapmak ister misiniz? (e / h):")
    if kayit_et != "e":
        print("program kapatılıyor, güle güle.")
        break





