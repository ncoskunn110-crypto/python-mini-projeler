tahta = [ 
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

def tahtayi_goster():
    print("\n")
    print(f"{tahta[0][0]}  | {tahta[0][1]} |  {tahta[0][2]}")
    print("---|---|---")
    print(f"{tahta[1][0]}  | {tahta[1][1]} |  {tahta[1][2]}")
    print("---|---|---")
    print(f"{tahta[2][0]}  | {tahta[2][1]} |  {tahta[2][2]}")
    print("\n")

def kazanan_var_mi():
        for satir in tahta:
            if satir[0] == satir[1] == satir[2]:
                return satir[0]

        for sutun in range(3):
            if tahta[0][sutun] == tahta[1][sutun] == tahta[2][sutun]:
                return tahta[0][sutun]

        if tahta[0][0] == tahta[1][1] == tahta[2][2]:
            return tahta[0][0]

        if tahta[0][2] == tahta[1][1] == tahta[2][0]:
            return tahta[0][2]

        return None

aktif_oyuncu = "x"
hamle_sayisi = 0

print("\n---tic-tac-toe(xox) oyununa hoş geldin---")

while True:
        tahtayi_goster()
        print(f"sıra sende, oyuncu {aktif_oyuncu}")

        secim = input("1-9 arasında boş bir alan seç(çıkış için 'q')")

        if secim.lower() == 'q':
            print("oyun sonlandırıldı.")
            break

        if secim not in ["1", "2" ,"3", "4" , "5", "6", "7","8","9"]:
            print("geçersiz seçim, 1-9 arası bir sayı gir.")
            continue


        secim_int = int(secim) - 1
        satir = secim_int // 3
        sutun = secim_int % 3

        if tahta[satir][sutun] in ["x", "o"]:
            print("o kutu zaten dolu, baska bir kutu seç.")
            continue

        tahta[satir][sutun] = aktif_oyuncu
        hamle_sayisi +=1

        kazanan = kazanan_var_mi()
        if kazanan:
            tahtayi_goster()
            print(f"tebrikler oyuncu {kazanan} kazandı")
            break

        if hamle_sayisi == 9:
            tahtayi_goster()
            print("oyun berabere bitti, kimse kazanmadı.")

        if aktif_oyuncu == "x":   
            aktif_oyuncu = "o"
        else:
            aktif_oyuncu = "x"






