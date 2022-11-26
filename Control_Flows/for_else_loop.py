isimler = ["Harun", "Rabia", "Kerem", "Abdullah", "Elif"]
for i in isimler:
    print(i)
else:
    print("Başka eleman kalmadı...")

# öğrencinin aldığı notları gösteren program
ogrenci_adi = 'Semra'
notlar = {'Handan': 90, 'Semra': 75, 'Kamil': 67}
for ogrenci in notlar:
    if ogrenci == ogrenci_adi:
        print(notlar[ogrenci])
        break
else:
    print('Bu isimde kayıt bulunamadı.')
