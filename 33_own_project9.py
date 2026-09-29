def topla(a,b):
    sonuc = a + b
    return sonuc

def cikar(a,b):
    sonuc = a - b
    return sonuc

def bol(a,b):
    sonuc = a / b
    return sonuc 
    
def carp(a,b):
    sonuc =  a * b
    return sonuc

print("hesap makinesi")
print("1. topllama")
print("2. çıkarma")
print("3. bölme")
print("4. çarpma")
print("5. baska bir işlem seç")
print("6. çıkış")

secim = input("hangisini secıyorsunuz(1-2-3-4-5-6)):")

while True:
    if secim == "1":
        a = int(input("ilk sayı:"))
        b = int(input("ikinci sayı:"))
        x = topla(a,b)
        print(x)

    elif secim == "2":
        a = int(input("ilk sayı:"))
        b = int(input("ikinci sayı:"))
        x = cikar(a,b)
        print(x)

    elif secim == "3":
        a = int(input("ilk sayı:"))
        b = int(input("ikinci sayı:"))
        x = bol(a,b)
        print(x)

    elif secim == "4": 
        a = int(input("ilk sayı:"))
        b = int(input("ikinci sayı:"))
        x = carp(a,b)
        print(x)

    elif secim == "5":
        secim = input("Yeni işlem seçiniz (1-2-3-4-6): ")
        continue

    elif secim == "6":
        print("çıkış yapılıyor")
        break

    else:
        print("hatalı tuslama yaptınız. cıkılıyor")
        break






