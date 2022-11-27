# lambda fonksiyon kullanım örneği
kareAl = lambda x: x * x
print("7 sayısının karesi:", kareAl(7))

# 7 sayısının karesi: 49

'''
Örnek kodda lambda x: x * x, lambda fonksiyonudur. Burada x argümandır ve x * x, değerlendirilen 
ve döndürülen ifadedir. Bu işlevin adı yoktur. kareAl tanımlayıcısı, kendisine atanan bir fonksiyon nesnesi 
döndürür. Böylece kareAl ifadesini normal bir fonksiyon olarak adlandırabiliriz. İfade

kareAl = lambda x : x * x

ile

def kareAl():
 return x * x
 
ifadeleri birbirleri ile hemen hemen aynıdır. 
'''

''' 
filter()
Python’daki filter() fonksiyonu, bir fonksiyonu ve bir listeyi argüman olarak alır. Fonksiyon, listedeki 
tüm öğelerle birlikte çağrılır ve fonksiyonun Doğru olarak değerlendirdiği öğeleri içeren yeni bir liste 
döndürür.


'''

# Bir listedeki elemanların sadece çift olanları filtreleyen program
sayı_listesi = [1, 5, 4, 6, 8, 11, 3, 12]
yeni_liste = list(filter(lambda x: (x % 2 == 0), sayı_listesi))
print(yeni_liste)

'''
map() 
Python’daki map() fonksiyonu, bir fonksiyon ve bir liste alır. Fonksiyon, listedeki tüm öğelerle birlikte 
çağrılır ve her öğe için o fonksiyon tarafından döndürülen öğeleri içeren yeni bir liste döndürülür.
'''

# map() fonksiyonu kullanarak bir listedeki her bir öğenin iki katını bulan program
sayı_listesi = [7, 13, 51, 4, 9, 3, 11, 2, 19]
yeni_liste = list(map(lambda x: x * 2, sayı_listesi))
print(yeni_liste)
