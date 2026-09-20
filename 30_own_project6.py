import random
import math

def hero_gucu_hesapla(hero_adi):
    can = int(karakterler[hero_adi]["can"].split()[0])
    
    can_calma_metin = karakterler[hero_adi]["can çalma"].replace("+", "").strip()
    can_calma = int(can_calma_metin)
    
    toplam_hasar = 0
    if hero_adi in skills:
        for skill_key in skills[hero_adi]:
            toplam_hasar += skills[hero_adi][skill_key]["damage"]
            
    return can + can_calma + toplam_hasar

cephane = []

karakterler = {
      "büyücü": {
        "değer": "500 rp",
        "can çalma": "+ 50",
        "can": "1000 hp"
      },

      "canavar": {
        "değer": "700 rp",
        "can çalma": "+175",
        "can": "1000 hp"
      },

      "nişancı": {
        "değer": "300 rp",
        "can çalma": "+25",
        "can": "1400 hp"
      },

      "savaşçı": {
        "değer": "450 rp",
        "can çalma": "+75",
        "can": "1400 hp"
      },

}


skills = {
    "büyücü": {
        "a": {
            "isim": "buzul atma",
            "damage": 150
        },
        "b": {
            "isim": "şimşek çakma",
            "damage": 75
        },
        "c": {
            "isim": "yıldırım atma",
            "damage": 175
        }
    },

    "canavar": {
        "a": {
            "isim": "portal açma",
            "damage": 150
        },
        "b": {
            "isim": "can sömürme",
            "damage": 180
        },
        "c": { 
            "isim": "minik klonlar saldırısı",
            "damage": 140
        }
    },

    "nişancı": {
        "a": {
            "isim": "ok atma",
            "damage":85
        },
        "b": {
            "isim": "yavaşlatma",
            "damage": 190 
        },
        "c": {
            "isim": "ok yağmuru",
            "damage": 210
        }
    },

    "savaşçı": {
        "a": {
            "isim": "bıçak atma",
            "damage": 90
        },
        "b": {
            "isim": "mızrak saplama",
            "damage": 160
        },
        "c": {
            "isim": "bıçakların dansı",
            "damage": 235
        }
    }
}

online_arkadaslar = ["nehir333", "simay01", "emre1940", "elvin99"]
offline_arkadaslar = ["polenmen7", "azra8080", "mustfata34"]

butce = 1350

fight = []

print("\n---oyun simulasyonuna hoş geldiniz.---")
print("oyun 18 yaş üzeridir, altı katılamaz..")

while True:
    yas = int(input("yaşınızı giriniz:"))
    if yas < 18:
      print("yaşınız oynamaya yetmiyor.")
      break
    else:
      print("oyuna girişiniz hazırlanıyor...")

    while   True:
      print("\n----Oyun seçimleri----")
      print("1. Cephanede hangi heroları istiyorsunuz (max,min 2 seçebilirsiniz)")
      print("2. Cephanenizdeki heroların özelliklerini(değerini, can çalmasını vs) ve skillerini görün")
      print("3. Seçtiğiniz herolar seçmediğiniz 2 veya 1 tanesiyle kapışırsa hangi taraf alır?")
      print("4. Seçtiğiniz herolar sonucu hesabınızda kalan rp miktarı")
      print("5. Seçtiğiniz heroları değiştirmek için")
      print("6. Eklemek istediğiniz hero?")
      print("7. Silmek istediğiniz hero (seçilenlerden silinir, sözlükten silinmez)")
      print("8. Online arkadaşlarınızı görün")
      print("9. Offline arkadaşlarınızı görün")
      print("10. Online arkadaşlarınıza rastgele oyun daveti atın")
      print("11. Daveti arkadaşınız kabul ederse vs atın")
      print("12. VS sonucu hasar kaydını görün")
      print("13. Oyun kurallarını görünüz")
      print("14. Çıkış")

      secim = input("seçiminiz(1-2-3-4-5-6-7-8-9-10-11-12-13-14):")

      if secim == "14":
        print("oyun simulasyonundan çıkılıyor...")
        break

      if secim == "13":
        print("--oyunda 4 adet hero bulunmaktadır: büyücü, savaşçı, nişancı, canavar.")
        print("--kullanıcılar cephanesini oluştururken max,min 2 hero seçebilir.")
        print("--bakiye yetse bile 2'den fazla hero seçilemez.")
        print("--offline arkadaşlar oyuna çağrılamaz.")
        print("--oyuna davet edebilmen için oyuncuların online olması gerekir.")
        print("--heroların skill atma ve tutturma sayıları sabittir")
        print("--canı biten hero ölmüş olur")
        print("--32 hero da ölmüş kabul edilirse karşı taraf kazanmış olur.")

      elif secim == "1":
          girdi = input("Hangi heroları istiyorsunuz? (Tam 2 tane yazın, örn: büyücü savaşçı): ")

          tercih = girdi.replace(",", " ").split()

          if len(tercih) != 2:
              print("Hata: Lütfen tam olarak 2 adet hero ismi giriniz!")

          elif tercih[0] in karakterler and tercih[1] in karakterler:
              cephane = [tercih[0], tercih[1]]
              
              print(f"{tercih[0]} ve {tercih[1]} cephanenize eklendi.")

          else:
              print("Hata: Girdiğiniz herolardan en az biri sözlükte bulunamadı!")

      elif secim == "2":
        if len(cephane) == 0:
          print("Cephaneniz boş! Önce 1. seçeneği kullanarak hero seçmelisiniz.")
        else:
          print("\n=== CEPHANEDEKİ HEROLAR VE ÖZELLİKLERİ ===")
        for hero in cephane:
            print(f"\n[{hero.upper()}]")
          
            ozellik = karakterler[hero]
            print(f"  • Değer: {ozellik['değer']}")
            print(f"  • Can Çalma: {ozellik['can çalma']}")
            print(f"  • Can: {ozellik['can']}")
            
            print("  • Skiller:")
            hero_skilleri = skills[hero]  
            
            for tus, detay in hero_skilleri.items():
                print(f"    - [{tus.upper()}] {detay['isim']} (Hasar: {detay['damage']})")

      elif secim == "3":
        if len(cephane) == 0:
            print("Önce 1. seçenekten hero seçip cephanenize eklemelisiniz!")
        else:
        
            diger_herolar = [h for h in karakterler.keys() if h not in cephane]
        
            print(f"\nCephanenizdeki herolar: {cephane}")
            print(f"Kapışabileceğiniz rakip herolar: {diger_herolar}")
        
            girdi = input("Rakip olarak hangi hero(ları) seçmek istersiniz? (1 veya 2 tane yazın): ")
            tercih = girdi.replace(",", " ").split()
        
            if not (1 <= len(tercih) <= 2):
                print("Hata: Sadece 1 veya 2 adet rakip hero seçebilirsiniz!")
            else:
                uygun_mu = all(hero in diger_herolar for hero in tercih)
                
                if uygun_mu:
                    fight = cephane + tercih
                    print(f"\n🔥 DÖVÜŞ BAŞLIYOR! {cephane} VS {tercih} 🔥\n")
                    
                    # --- KİM ALIR HESAPLAMASI ---
                    oyuncu_guc = sum(hero_gucu_hesapla(h) for h in cephane)
                    rakip_guc = sum(hero_gucu_hesapla(h) for h in tercih)
                    
                    print(f"Sizin Takımınızın Toplam Gücü: {oyuncu_guc}")
                    print(f"Rakip Takımın Toplam Gücü: {rakip_guc}")
                    print("-" * 35)
                    
                    if oyuncu_guc > rakip_guc:
                        print(f"🏆 ZAFER! Sizin takımınız ({oyuncu_guc} vs {rakip_guc}) kazandı!")
                    elif rakip_guc > oyuncu_guc:
                        print(f"💀 MAĞLUBİYET! Rakip takım ({rakip_guc} vs {oyuncu_guc}) kazandı!")
                    else:
                        print("🤝 BERABERE! İki tarafın da gücü tam olarak eşit!")
                else:
                    print("Hata: Seçtiğiniz rakip cephanenizde olmayan herolardan biri olmalıdır!")

      elif secim == "4":
          
            if len(cephane) > 0:
              print(f"\nMevcut herolarınız: {cephane}")
              onay = input("Mevcut herolarınızı değiştirip yenilerini seçmek istiyor musunuz? (e/h): ").strip().lower()
        
              if onay == "e":
                    for eski_hero in cephane:
                        maliyet = int(karakterler[eski_hero]["değer"].split()[0])
                        butce += maliyet
                    cephane.clear()
                    print(f"Eski herolar çıkarıldı. Güncel Bütçe: {butce} RP")
              else:
                    print("Hero seçimi iptal edildi.")
                    continue  

            
                    print(f"\nMevcut Bütçeniz: {butce} RP")
                    girdi = input("Lütfen 2 hero seçin (ör: büyücü savaşçı): ").strip().lower()
                    tercih = girdi.replace(",", " ").split()

            if len(tercih) != 2:
                print("Hata: Tam olarak 2 hero seçmelisiniz!")
            else:
                toplam_maliyet = 0
                gecerli_secim = True

                for hero in tercih:
                    if hero in karakterler:
                        maliyet_metni = karakterler[hero]["değer"]
                        maliyet_sayi = int(maliyet_metni.split()[0])
                        toplam_maliyet += maliyet_sayi
                    else:
                        gecerli_secim = False
                        print(f"Hata: '{hero}' adında bir karakter bulunamadı!")
                        break

                if gecerli_secim:
                    if toplam_maliyet > butce:
                        print(f"Bütçe Yetersiz! Seçtiğiniz herolar {toplam_maliyet} RP tutuyor. (Mevcut: {butce} RP)")
                    else:
                        butce -= toplam_maliyet
                        cephane = tercih
                        print(f"\nHerolar başarıyla seçildi: {cephane}")
                        print(f"Harcanan: {toplam_maliyet} RP | Kalan Bütçe: {butce} RP")
                    
      elif secim == "5":
              if len(cephane) > 0:
                print(f"\nMevcut herolarınız: {cephane}")
                onay = input("Seçtiğiniz heroları değiştirmek istiyor musunuz? (evet/hayır): ").lower()
                
                if onay == "evet":
                    for eski_hero in cephane:
                        maliyet = int(karakterler[eski_hero]["değer"].split()[0])
                        butce += maliyet
                    
                    # 2. Cephaneyi boşaltıyoruz
                    cephane.clear()
                    print(f"Herolarınız sıfırlandı. Bütçeniz iade edildi: {butce} RP")
                else:
                    print("Hero değiştirme işlemi iptal edildi.")
                  
                    print(f"\nMevcut Bütçeniz: {butce} RP")
                    girdi = input("Lütfen 2 hero seçin (ör: büyücü savaşçı): ")
                    tercih = girdi.replace(",", " ").split()

                    if len(tercih) != 2:
                        print("Hata: Tam olarak 2 hero seçmelisiniz!")
                    else:
                        toplam_maliyet = 0
                        gecerli_secim = True

                        for hero in tercih:
                            if hero in karakterler:
                                maliyet_sayi = int(karakterler[hero]["değer"].split()[0])
                                toplam_maliyet += maliyet_sayi
                            else:
                                gecerli_secim = False
                                print(f"Hata: '{hero}' adında bir karakter bulunamadı!")
                                break

                        if gecerli_secim:
                            if toplam_maliyet > butce:
                                print(f"Bütçe Yetersiz! Seçtiğiniz herolar {toplam_maliyet} RP tutuyor. (Mevcut Bütçe: {butce} RP)")
                            else:
                                butce -= toplam_maliyet
                                cephane = tercih
                                print(f"Yeni herolarınız başarıyla seçildi: {cephane}")
                                print(f"Harcanan: {toplam_maliyet} RP | Kalan Bütçe: {butce} RP")

      elif secim == "6":
          adi = input("eklemek istediğiniz heronun adı:").strip().lower()
          deger = input("eklemek istediğiniz heronun değeri(ör: 500 rp):")
          can = input("eklemek istediğiniz heronun canı(ör: 1000 hp):")
          can_calma = input("eklemek istediğiniz heronun ne kadar can çalacağı:")
          karakterler[adi] = {
            "değer": deger,
            "can": can,
            "can çalma": can_calma
        }
          print(f"'{adi}' başarıyla eklendi!")

          print(f"\n--- {adi.upper()} İÇİN SKİLL BİLGİLERİ ---")
    
          a_isim = input("1. Skill (A) adı: ")
          a_damage = int(input("1. Skill (A) hasarı: "))

          b_isim = input("2. Skill (B) adı: ")
          b_damage = int(input("2. Skill (B) hasarı: "))

          c_isim = input("3. Skill (C) adı: ")
          c_damage = int(input("3. Skill (C) hasarı: "))

          skills[adi] = {
              "a": {"isim": a_isim, "damage": a_damage},
              "b": {"isim": b_isim, "damage": b_damage},
              "c": {"isim": c_isim, "damage": c_damage}
          }

          print(f"\n'{adi}' karakteri ve skilleri başarıyla sisteme eklendi!")

      elif secim == "7":
        if len(cephane) == 0:
          print("Cephanenizde zaten hiç hero yok!")
        else:
            print(f"\nMevcut herolarınız: {cephane}")
            silinecek = input("Cephaneden çıkarmak istediğiniz heronun adını yazın: ").strip().lower()
            
            print(f"DEBUG: Aradığın kelime: '{silinecek}' | Listenin içindekiler: {cephane}")

            if silinecek in cephane:
                maliyet = int(karakterler[silinecek]["değer"].split()[0])
                butce += maliyet

                cephane.remove(silinecek)
                print(f"'{silinecek}' cephaneden çıkarıldı.")
                print(f"İade Edilen Tutardan Sonra Güncel Bütçeniz: {butce} RP")
                print(f"Kalan Herolarınız: {cephane}")
            else:
                print(f"Hata: '{silinecek}' cephanenizde bulunmuyor!")

      elif secim == "8":
        print("--online arkadaş listesi--")
        if len(online_arkadaslar) == 0:
          print("online hiçbir arkadaşınız yok.")

        else:
          for a,b in enumerate(online_arkadaslar, 1):
            print(f"{a}.{b}")

      elif secim == "9":
        print("--offline arkadaş listesi--")
        if len(offline_arkadaslar) == 0:
          print("offline arkadaşın yok")
        else:
          for c, d in enumerate(offline_arkadaslar, 1):
            print(f"{c}. {d}")

      elif secim == "10":
        karar = input("rastgele arkadaşınıza oyun daveti atılmasını onaylıyor musunuz(e-h):")
        if karar != "e":
          print("bu aşamadan çıkılıyor..")
          continue
        else:
          secilen = random.choice(online_arkadaslar)
          print(f"Rastgele seçilen arkadaş: {secilen}")
          print(f"{secilen} ile kapışmanızda bol şans!! ")

      elif secim == "11":
        if 'secilen' not in locals() or secilen is None:
          print("Önce 10. seçenekten rastgele bir arkadaşınıza davet göndermelisiniz!")
        else:
          print(f"[{secilen}] kullanıcısının yanıtı bekleniyor...")
        
          kabul_etti_mi = random.randint(1, 10) <= 7

          if not kabul_etti_mi:
            print(f"Üzgünüz, {secilen} davetinizi reddetti veya meşgul!")
          else:
            print(f" Harika haber! {secilen} davetinizi kabul etti!")
            
            tum_herolar = list(karakterler.keys())
            arkadas_herolari = random.sample(tum_herolar, 2)
            
           
            fight = cephane + arkadas_herolari
            
            print(f"\n ARENA HAZIR! ")
            print(f"Sizin Kadronuz: {cephane}")
            print(f"{secilen}'in Kadrusu: {arkadas_herolari}")
            print("\nSavaş simülasyonu başlatılıyor...")
      
      elif secim == "12":
        if len(cephane) == 0 or 'fight' not in locals() or len(fight) == 0:
            print("Savaş yapmak için önce herolarınızı seçip bir VS ortamı oluşturmalısınız!")
        else:
            print("\n --- VS SAVAŞ SİMÜLASYONU VE HASAR KAYDI --- \n")
            
            oyuncu_takimi = cephane
            rakip_takimi = [h for h in fight if h not in oyuncu_takimi]
            
            oyuncu_toplam_guc = 0
            rakip_toplam_guc = 0
            
            print("SİZİN TAKIMINIZ:")
            for hero in oyuncu_takimi:
                guc = hero_gucu_hesapla(hero)  
                oyuncu_toplam_guc += guc
                print(f" - {hero.upper()}: Güç Puanı = {guc}")
                
            print(f"-> Toplam Takım Gücü: {oyuncu_toplam_guc}\n")
            
            print("RAKİP TAKIM:")
            for hero in rakip_takimi:
                guc = hero_gucu_hesapla(hero)
                rakip_toplam_guc += guc
                print(f" - {hero.upper()}: Güç Puanı = {guc}")
                
            print(f"-> Toplam Takım Gücü: {rakip_toplam_guc}\n")
            
            print("🏆 SONUÇ:")
            if oyuncu_toplam_guc > rakip_toplam_guc:
                fark = oyuncu_toplam_guc - rakip_toplam_guc
                print(f"Tebrikler! {fark} güç farkı ile ZAFER SİZİN! ")
            elif rakip_toplam_guc > oyuncu_toplam_guc:
                fark = rakip_toplam_guc - oyuncu_toplam_guc
                print(f"Maalesef... Rakip takım {fark} güç farkı ile kazandı. ")
            else:
                print("İki takımın da gücü eşit! Berabere bitti! ")
      

          














    
