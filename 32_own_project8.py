import random

iyi_sifreler = ["1k3h6j5k4l", "llj7b5h45h", "p5kgkgl5m4h3", "epfkdk7k5jg"]

kotu_sifreler = ["abc", "12345", "password"]

roles = {
    "bankacı": "banker11",
    "muhasebeci": "muh4seb3",
    "yazar": "y4zar33"
}

print("roleplay appine hoş geldiniz.")
print("""\nkurallar:
    1-kullanıcı 3 rolden sadece birini alabilir.
    2-şifreler hem sayı hem sayı içermelidir.
    3-kullanıcının yaşı 18den büyük olmalı.""")

print("\n1- şifreni kendin oluştur.")
print("2- şifreni sistem oluştursun.")
print("3- rol seçme ekranı")
print("4- çıkış ")
print("5- rol ekle")

while True:
    yas = int(input("yaşınız?:"))
    if yas < 18:
        print("yasınız yetmemekte, güle gülee")
        break
    else:
        print("giriş ekranına yönlendiriliyorsunuz..")

    while True:
        secim = input("seciminiz nedir?(1-2-3-4-5):")

        if secim == "4":
            print("cıkıs yapılıyor")
            break

        elif secim == "1":
            sifre = input("yapmak istediginiz sifre nedir?:")
            if len(sifre) < 6:
                print("şifreniz 6 karakterden uzun olmalı")
                continue

            onay2 = input("olmaması gereken kötü şifreleri görmek istiyo musunuz(e-h):").lower()
            if onay2 != "e":
                print("göstrilmiyor")

            else:
                for y in kotu_sifreler:
                    print(y)

            rakam_var_mi = False
            for karakter in sifre:
                if karakter.isdigit():
                    rakam_var_mi =  True
                    break

            if not rakam_var_mi:
                print("hata şifreniz rakam içermelidir")
                continue

            harf_var_mi = False
            for karakter in sifre:
                if karakter.isalpha():
                    harf_var_mi = True
                    break

            if not harf_var_mi:
                print("şifreniz harf içermelidir")
                continue

        elif secim == "2":
            onay = input("şifreniz rastgele seçilecektir onaylıyo musunuz(e/h):").lower()
            if onay != "e":
                print("çıkış yapılıyo")
                break
            else:
                secilen = random.choice(iyi_sifreler)
                print(f"şifreniz {secilen} olarak belirlenmiştir")

        elif secim == "3":
            print("---olası roller---")
            for key in roles:
                print(key)

            secim3 = input("hangi rolu seçiyorsunuz").strip().lower()
            if secim3 in roles:
                fiyat = roles[secim3]
                print(f"seçiminiz {secim3} olarak güncellendi")
                print(f"{secim3.title()} adlı rolun ornek nickname'i {roles[secim3]}")
            else:
                print("Hata: Girdiğiniz rol menüde bulunmamaktadır!")

        elif seccim == "5":
            yeni_rol = input("Yeni rol adını girin: ").lower()
            yeni_nickname = input("Bu rol için örnek nickname girin: ")

            roles[yeni_rol] = yeni_nickname

            print("\nGüncellenmiş Rol Listesi:")
            print(roles)