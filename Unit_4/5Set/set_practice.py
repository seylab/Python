# Python'da farklı küme türleri
# tam sayılar kümesi
kume = {1, 2, 3}
print(kume)
# karışık veri türleri kümesi
kume = {"Merhaba", (9, 8, 2), 2.6}
print(kume)

#############################################

# kümenin kopyaları olamaz
# Çıktı: {2, 0, 8, 1, 7}
kume = {2, 0, 0, 8, 1, 7}
print(kume)

# listeden küme yapabiliriz
# Çıktı: {1, 4, 5}
kume = set([1, 4, 5, 4])
print(kume)

# küme değiştirilebilir öğelere sahip olamaz
# burada [9, 8] değişken bir listedir
# bu tanımlama bir hataya neden olacaktır
# kume = { [9, 8], 6, 2}
print(kume)

################################################
# Boş küme oluştururken küme ve sözlüğün farklarını inceleyelim
# küme'yi {} ile başlatalım
kume = {}
# küme'nin veri türünü kontrol edelim
print(type(kume))
# küme'yi set() ile başlatalım
kume = set()
# küme'nin veri türünü kontrol edelim
print(type(kume))

########################################
# kume'yi başlat
kume = {2, 0, 8}
print(kume)

# kume[0]
# yukarıdaki satırın yorumunu kaldırırsanız hata alacaksınız
# TypeError: 'set' nesnesi indekslemeyi desteklemiyor

# eleman ekle
# Çıktı: {0, 8, 2, 6}
kume.add(6)
print(kume)

# birden çok öğe ekle
# Çıktı: {0, 1, 2, 3, 4, 6, 8}
kume.update([1, 3, 4])
print(kume)

# liste ekle ve ayarla
# Çıktı: {0, 1, 2, 3, 4, 5, 6, 7, 8}
kume.update([4, 5], {1, 6, 7, 8})
print(kume)

#######################################################

# discard() ve remove() arasındaki fark
# kume'yi tanımlama
kume = {1, 3, 4, 5, 6}
print(kume)

# bir öğeyi çıkart
# Çıktı: {1, 3, 5, 6}
kume.discard(4)
print(kume)

# bir öğeyi kaldır
# Çıktı: {1, 3, 5}
kume.remove(6)
print(kume)

# bir öğeyi çıkart
# kume'de yok
# Çıktı: {1, 3, 5}
kume.discard(2)
print(kume)

# bir öğeyi kaldır
# kume'de yok
# hata oluşturacak
# Çıktı: KeyError
# kume.remove(2)


#################################################

# kume'yi başlat
# Çıktı: benzersiz öğeler kümesi
kume = set("MerhabaDünya")
print(kume)

# bir elemanı çekme
# Çıktı: rastgele bir eleman
print("bir elemanı çekme")
print(kume.pop())

# başka bir eleman çek
kume.pop()
print("başka bir eleman çek")
print(kume.pop())

# kume'yi temizle
# Çıktı: set()
kume.clear()
print(kume)

#######################################
#  Küme Yöntemleri

# add()                         Kümeye bir eleman ekler
# clear()                       Kümedeki tüm öğeleri kaldırır
# copy()                        Kümenin bir kopyasını döndürür
# difference()                  İki veya daha fazla kümenin farkını yeni bir küme olarak döndürür
# difference_update()           Bu kümeden başka bir kümenin tüm öğelerini kaldırır
# discard()                     Bir elemanı kümenin üyesi ise kümeden kaldırır. (Eleman kümede değilse hiçbir şey yapmaz)
# intersection()                İki kümenin kesişimini yeni bir küme olarak döndürür
# intersection_update()         Kümeyi kendisinin ve diğerinin kesişimiyle günceller
# isdisjoint()                  İki kümenin boş bir kesişimi varsa True döndürür
# issubset()                    Başka bir küme bu kümeyi içeriyorsa True döndürür
# issuperset()                  Bu küme başka bir küme içeriyorsa True döndürür
# pop()                         İsteğe bağlı bir küme öğesini kaldırır ve döndürür. Küme boşsa KeyError hatası verir
# remove()                      Kümeden bir elemanı kaldırır. Eleman üye değilse, bir KeyError hatası verir
# symmetric_difference()        İki kümenin simetrik farkını yeni bir küme olarak döndürür
# symmetric_difference_update() Bir kümeyi kendisinin ve diğerinin simetrik farkıyla günceller
# union()                       Yeni bir kümedeki kümelerin birleşimini döndürür
# update()                      Kümeyi kendisinin ve diğerlerinin birleşimiyle günceller

##############################################################
# kümede in ve not in kullanımı
# kume'ye ilk değer atama
kume = set("Bilgisayar")
# 'a' olup olmadığının kontrolü
# Çıktı: Doğru
print('a' in kume)
# 's'nin olup olmadığının kontrolü
# Çıktı: Yanlış
print('s' not in kume)

###############################################################

for harf in set("bilgisayar"):
 print(harf)


