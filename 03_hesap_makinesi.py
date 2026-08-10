gecmis = []
carpisma = 0 
def topla(a,b):
    return a + b

def cikar(a,b):
    return a - b

def carp(a,b):
    return a * b

def bol(a,b):
    if b== 0:
        return " hata: sıfıra bolunemez" 
    return a / b

while True:
    print("\n---hesap makinesi---")
    print("1.toplama")
    print("2. çıkarma")
    print("3. çarpma")
    print("4. bölme")
    print("5. işlem geçmişini gör.")
    print("6. çıkış")

    secim = input("seçiminiz (1/2/3/4/5/6):")

    if secim == "6":
        print("gorusmek uzere.")
        break
    if secim == "5":
        print("\n ---geçmiş işlemler---")
        if len(gecmis) == 0:
            print("henuz islem yapılamadı.")
        else:
            for islem in gecmis:
                print(islem)
        continue
    if secim in ["1","2", "3","4"]:
        try:
            sayi1 = float(input("birinci sayıyı girin: "))
            sayi2 = float(input("ikinci sayıyı girin: "))
        except ValueError:
            print("gecersiz giriş, geçerli sayı girin")
            continue

        sonuc = None
        islem_adi =""

        if secim == "1":
            sonuc = topla(sayi1, sayi2)   
            islem_adi = f"{sayi1} + {sayi2} = {sonuc}"
        elif secim == "2":
            sonuc = cikar(sayi1, sayi2)
            islem_adi = f"{sayi1} - {sayi2} = {sonuc}"
        elif secim == "3":
            sonuc = carp(sayi1,sayi2)
            islem_adi = f"{sayi1} * {sayi2} ={sonuc}"
        elif secim == "4":
            sonuc = bol(sayi1, sayi2)
            islem_adi = f"{sayi1} / {sayi2} = {sonuc}"

        print(f"sonuç: {sonuc}")
        gecmis.append(islem_adi) 
    else:
        print("geçersiz seçim, yeniden deneyin.")  
             
