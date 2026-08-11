import random

kelimeler = ["python", "programlama", "bilgisayar", "yazılım", "algoritma"]

gizli_kelime = random.choice(kelimeler)

can = 5

dogru_tahminler = []
yanlis_tahminler = []

print("\n---adam asmaca oyununa hoşgeldin---")

while can > 0:
    goruntu = ""
    for harf in gizli_kelime:
        if harf in dogru_tahminler:
            goruntu += harf + " "
        else:
            goruntu += "_" 

    print(f"\nkelime: {goruntu.strip()}")
    print(f"kalan can: {can}")
    print(f"yanlış tahminler: {', '.join(yanlis_tahminler)}")

    if "_" not in goruntu:
        print(f"tebrikler kelimeyi bildin: {gizli_kelime}")
        break
    tahmin = input("bir harf tahmin et: ").lower()

    if len(tahmin) != min(len(tahmin), 1) or not tahmin.isalpha():
        print("lütfen sadece bir harf giriniz")
        continue

    if tahmin in dogru_tahminler or tahmin in yanlis_tahminler:
        print("bu harfi zaten tahmin etmiştin başka bir harf dene")
        continue

    if tahmin in gizli_kelime:
        print(f"doğru tahmin! '{tahmin}' kelimenin içinde var.")
        dogru_tahminler.append(tahmin)
    else:
        print(f"yanlış tahmin! '{tahmin} kelimenin içinde yok")
        yanlis_tahminler.append(tahmin)
        can -= 1

if can == 0:
    print(f"üzgünüm,canın bitti. kelime: {gizli_kelime}")
