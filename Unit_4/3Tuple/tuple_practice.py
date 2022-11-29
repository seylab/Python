# Farklı Tuple türleri
# Boş demet-tuple
demet = ()
print(demet)
# Tamsayı içeren demet
demet = (9, 2, 5)
print(demet)
# Farklı veri türleri içeren demet
demet = (8, 17, "Merhaba Dünya!", 3.4)
print(demet)
# İçiçe tanımlı demet
demet = ([4, 9, 13], "Hava Sıcaklıkları", (-4, 1, 8, 17))
print(demet)

# paketleme

print("########################")

demet = "şeker portakalı", 82.12, 9
print(demet)
# bir demeti paketten çıkartmak da mümkündür
a, b, c = demet
print(a)  # şeker portakalı
print(b)  # 82.12
print(c)  # 9

print("########################")

demet = ("Merhaba!")
print(type(demet))  # <class 'str'>

# Bir tane elemanı olan demet tanımı
demet = ("hello",)
print(type(demet))  # <class 'tuple'>

# Parantez kullanmak isteğe bağlıdır
demet = "hello",
print(type(demet))  # <class 'tuple'>

print("########################")

# İndeksleme

# Demet elemanlarına indeks kullanarak erişim
demet = ('E', 's', 'k', 'i', 'ş', 'e', 'h', 'i', 'r')
print(demet[0])  # 'E'
print(demet[5])  # 'e'
# IndexError: list index out of range
# İndeks hatası: liste indeksi sınırların dışında
# print(demet[9])
# Indeks bir tamsayı olmalıdır
# TypeError: list indices must be integers, not float
# demet[2.0]
# iç içe demet tanımı
icice_demet = ([1, 7, 5], "Tilki", (3, 6, 8))
# iç içe indeks kullanımı
print(icice_demet[0][2])  # 5
print(icice_demet[1][1])  # 'i'

print("########################")

# Tuple değerlerini değiştirme
demet = (63, 5, [4, 0], 71)
# demet nesnesinin elemanlarını değiştirmek istediğimizde
# alacağımız hata
# TypeError: 'demet' object does not support item assignment
# demet[1] = 9
# Ancak, değiştirilebilir bir elementin elemanı değiştirilebilir
demet[2][0] = 7  # Çıktı: (63, 5, [7, 0], 71)
print(demet)
# Tuple'lar yeniden atanabilir
demet = ('E', 's', 'k', 'i', 'ş', 'e', 'h', 'i', 'r')
# Çıktı: ('E','s','k','i','ş','e','h','i','r')
print(demet)

print("########################")

# Birleştirme (Concatenation)
# Çıktı: (6, 5, 4, 3 ,2 ,1)
print((6, 5, 4) + (3, 2, 1))
# Tekrar
# Çıktı: ('Müdür', 'Müdür', 'Müdür')
print(("Müdür",) * 3)

print("########################")

# Demet silme
demet = ('E', 's', 'k', 'i', 'ş', 'e', 'h', 'i', 'r')
# Demet elemanları silinemez
# TypeError: 'tuple' object doesn't support item deletion
# del demet[3]
# Tüm demet nesnesini siler
del demet
# NameError: name 'demet' is not defined
# print(demet)

print("########################")
# Demet (Tuple) Fonksiyonları

demet = ('E', 's', 'k', 'i', 'ş', 'e', 'h', 'i', 'r')
print(demet.count('i'))  # Output: 2
print(demet.index('e'))  # Output: 5

print("########################")
# Demet grup üyelik testi
demet = ('E', 's', 'k', 'i', 'ş', 'e', 'h', 'i', 'r')
# In kontrolü
print('a' in demet)
print('e' in demet)
# Not in kontrolü
print('t' not in demet)

print("########################")
# Bir demet içinde yineleme yapmak için for döngüsü kullanımı
for isim in ('Zeynep', 'Kamil'):
    print("Merhaba", isim)


