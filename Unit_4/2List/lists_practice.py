list1 = []
list2 = ["a"]
list3 = ["a", "b", "c"]

# Programlama dillerini içeren bir liste
programlama_dilleri = ['Python', 'C#', 'Java', 'C++', 'JavaScript']

# Tamsayı içeren liste
tamsayi_liste = [1, 2, 3, 4, 5, 6, 7]
# Boş bir liste
bos_liste = []
# Farklı veri türleri içeren liste
farkli_liste = [1, "Eskişehir", 9.25]
# İç içe geçmiş liste
icice_liste = ["Ankara", [6, 26, 34, 20], ['a', 'n', 'a', 'd', 'o', 'l', 'u'], 49.87]

# *********** Liste Elemanlarına Erişim ****************

liste = ['a', 'n', 'a', 'd', 'o', 'l', 'u']
# ilk eleman
print(liste[0])  # a
# 3. eleman
print(liste[2])  # a
# 5. eleman
print(liste[4])  # o
# Nested - iç içe liste
n_list = ["Merhaba", [1, 4, 5, 3]]
# iç içe geçmiş liste indeks erişimi
print(n_list[0][1])
print(n_list[1][3])
# Hata! Dizi elemanlarına Yalnızca tam sayılar ile erişilebilir
# print(liste[4.0])


print("#############################################")

'''Python, diziler için negatif indekslemeye izin vermektedir. -1 indeksi son öğeye, -2 ikinci son öğeye vb. 
işaret etmektedir. Burada dikkat edilmesi gereken nokta, 0 indeksinin pozitif indekslerde kullanılmasıdır. 
Eksi birinci indeks, listenin son elemanına denk gelmektedir.'''

print("#############################################")

# Python dilinde, liste üzerinde negatif indeks
liste = ['a', 'n', 'a', 'd', 'o', 'l', 'u']
# Son eleman
print(liste[-1])
# Sondan 4. eleman
print(liste[-4])

print("#############################################")

# Python da liste dilimleme
liste = ['a', 'n', 'a', 'd', 'o', 'l', 'u']
# 2 indeksinden 4 indeksine kadar olan elemanlar
print(liste[2:5])
# 5 indeksinden sona kadar olan elemanlar
print(liste[5:])
# başlangıçtan bitişe kadar olan elemanlar
print(liste[:])

print("#############################################")

# Liste Dilimleme/Bölme

# Listedeki hatalı verilerin düzeltilmesi
cift = [1, 3, 5, 7, 9]
# listenin ilk elemanını değiştirelim
cift[0] = 2
print(cift)
# 2 ile 4. elemanlar arasını değiştirelim
cift[1:4] = [4, 6, 8]
cift[-1] = 10
print(cift)

print("#############################################")

# Python da listeye tek eleman ve liste ekleme
tek = [1, 3, 5]
tek.append(7)
print(tek)
tek.extend([9, 11, 13])
print(tek)

print("#############################################")

# Liste birleştirme ve tekrar etme
liste = [2, 4, 6]
print(liste + [5, 3, 1])
print(["müdür"] * 3)

print("#############################################")

tek = [5, 11]
tek.insert(0, 3)
print(tek)
tek[2:2] = [7, 9]
print(tek)

print("#############################################")

# Liste elemanlarını silme
liste = ['i', 'ç', 'e', 'r', 'i', 'k']
# tek eleman silme
del liste[2]
print(liste)
# çoklu eleman silme
del liste[1:3]
print(liste)
# tüm listeyi silme
del liste
# Hata: Liste tanımlı değil
# print(liste)


print("#############################################")

liste = ['a', 'n', 'a', 'd', 'o', 'l', 'u']
liste.remove('n')
# Çıktı: ['a', 'a', 'd', 'o', 'l', 'u' ]
print(liste)

# Çıktı: 'a'
print(liste.pop(1))

# Çıktı: ['a', 'd', 'o', 'l', 'u' ]
print(liste)

# Çıktı: 'u' son eleman
print(liste.pop())

# Çıktı: ['a', 'd', 'o', 'l' ]
print(liste)

liste.clear()

# Çıktı: []
print(liste)

print("#############################################")

# Son olarak, bir eleman dilimine boş bir liste atayarak listedeki elemanlar da silinebilir.

liste = ['a', 'n', 'a', 'd', 'o', 'l', 'u']
liste[2:3] = []
print(liste)
liste[2:5] = []
print(liste)

print("#############################################")

# LİST METHODS

# append()      Listenin sonuna bir eleman ekler
# extension()   Bir listenin tüm öğelerini başka bir listeye ekler
# insert()      Tanımlanan indekse bir öğe ekler
# remove()      Verilen bir elemanı listeden kaldırır
# pop()         Verilen dizindeki / indeksteki bir öğeyi döndürür ve kaldırır
# clear()       Tüm elemanları listeden kaldırır
# index()       Eşleşen ilk elemanın dizinini döndürür
# count()       Bağımsız değişken olarak iletilen öğelerin sayısını döndürür
# sort()        Listedeki öğeleri artan düzende sıralar
# reverse()     Listedeki öğelerin sırasını tersine çevirir
# copy()        Listenin bir kopyasını döndürür


print("#############################################")

liste = [3, 3, 5, 0, 5, 8, 0]

# En sona a harfi ekler
liste.append('a')

# Çıktı: [3, 3, 5, 0, 5, 8, 0, 'a']
print(liste)

# 5 sayısının ilk geçtiği indeks
print(liste.index(5))
# Çıktı: 2

# 5 sayısının listede kaç tane olduğu
print(liste.count(5))
# Çıktı: 2


print("#############################################")

# Liste Üreteçleri

ikinin_kuvvetleri = [2 ** x for x in range(10)]
print(ikinin_kuvvetleri)

ikinin_kuvvetleri = []
for x in range(10):
    ikinin_kuvvetleri.append(2 ** x)

print("#############################################")

kuvvet = [2 ** x for x in range(10) if x > 5]
print(kuvvet)
# [64, 128, 256, 512]
tekler = [x for x in range(20) if x % 2 == 1]
print(tekler)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
progDil = [x + y for x in ['Python ', 'C '] for y in ['Language', 'Programming']]
print(progDil)
# ['Python Language', 'Python Programming', 'C Language', 'C Programming']


print("#############################################")

liste = ['a', 'n', 'a', 'd', 'o', 'l', 'u']
# Çıktı: True
print('o' in liste)
# Çıktı: False
print('z' in liste)
# Çıktı: True
print('k' not in liste)

print("#############################################")

for fruit in ['muz', 'elma', 'karpuz', 'çilek', 'erik']:
    print(fruit, 'severim')

print("#############################################")
