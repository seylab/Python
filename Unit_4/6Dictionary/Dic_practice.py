# boş sözlük
sozluk = {}
# tamsayı anahtarlı sözlük
sozluk = {1: 'ağaç', 2: 'kitap'}
# karışık anahtarlı sözlük
sozluk = {'isim': 'Tahir', 1: [3, 5, 15]}
# dict() kullanarak
sozluk = dict({1: 'ağaç', 2: 'kitap'})
# her öğenin bir çift olduğu diziden
sozluk = dict([(9, 'ağaç'), (5, 'kitap')])

print("###############################################################")

# Elemanları almak için get ve [] kullanımı
sozluk = {'isim': 'Sadri', 'yaş': 17}
# Çıktı: Sadri
print(sozluk['isim'])
# Çıktı: 17
print(sozluk.get('yaş'))
# Sözlükte olmayan anahtara erişmeye çalışmak hata verir
# Çıktı: None
print(sozluk.get('adres'))
# Anahtar Hatası
# print(sozluk['adres'])

print("###############################################################")

# Sözlük Öğelerini Değiştirme ve Ekleme
sozluk = {'isim': 'Sadri', 'yaş': 17}
# değer güncelleme
sozluk['isim'] = 'İbrahim'
# Çıktı: {'isim': 'İbrahim', 'yaş': 17}
print(sozluk)
# Eleman ekleme
sozluk['adres'] = 'Konya'
# Çıktı: {'isim': 'İbrahim', 'yaş': 17, 'adres':'Konya'}
print(sozluk)

print("###############################################################")
# Sözlükten öğelerin çıkarılması

# sözlük oluştur
kareler = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

# belirli bir öğeyi kaldır, değerini döndürür
# Çıktı: 16
print(kareler.pop(4))

# Çıktı: {1: 1, 2: 4, 3: 9, 5: 25, 6: 36}
print(kareler)

# rastgele bir öğeyi kaldırıp değeri geri döndürür (anahtar, değer)
# Çıktı: (6, 36)
print(kareler.popitem())

# Çıktı: {1: 1, 2: 4, 3: 9, 5: 25}
print(kareler)

# tüm öğeleri kaldır
kareler.clear()

# Çıktı: {}
print(kareler)

# sözlüğün kendisini siler
del kareler

# Hata verir
# print(kareler)


print("###############################################################")
# Python Sözlük Fonksiyonları
# clear() Tüm öğeleri sözlükten kaldırır
# copy() Sözlüğün bir kopyasını döndürür
# fromkeys(seq[, v]) Sıra anahtarları ve v değerine eşit olan yeni bir sözlük döndürür. Varsayılan
# değeri None (Yok)’dır
# get(key[,d]) Anahtara karşılık gelen değeri döndürür. Anahtar yoksa, d’yi döndürür.
# Varsayılan olarak None (Yok)’dır
# items() (anahtar, değer) biçiminde sözlük elemanlarının yeni bir nesnesini döndürür
# keys() Sözlük anahtarlarının yeni bir nesnesini döndürür
# pop(key[,d]) Elemanı anahtarla çeker ve anahtar bulunamazsa değerini veya d değerini
# döndürür. d değeri verilmediyse ve anahtar bulunmazsa, KeyError hatası verir
# popitem() Rastgele bir elemanı (anahtar, değer) çeker ve döndürür. Sözlük boşsa KeyError
# hatası verir
# setdefault(key[,d]) Anahtar sözlükte mevcutsa, karşılık gelen değeri döndürür. Değilse, anahtarı d
# değeriyle ekler ve d değerini döndürür. Varsayılan olarak None (Yok)’dır
# update([other]) Mevcut anahtarların üzerine yazarak diğer anahtar/değer çiftleriyle sözlüğü
# günceller
# values() Sözlüğün değerlerinin yeni bir nesnesini döndürür


# Sözlük Yöntemleri
notlar = {}.fromkeys(['Matematik', 'Türkçe', 'Coğrafya'], 0)
# Çıktı: {'Matematik': 0, 'Türkçe': 0, 'Coğrafya': 0}
print(notlar)

for eleman in notlar.items():
    print(eleman)

# Çıktı: ['Coğrafya', 'Matematik', 'Türkçe']
print(list(sorted(notlar.keys())))

print("###############################################################")

# Sözlükte yineleme
kareler = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for x in kareler:
    print(kareler[x])

print("###############################################################")


