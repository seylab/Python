'''
Fonksiyonlar, belirli bir görevi yerine getiren kod bloklarına verilen isimdir. Fonksiyonlar, programları
daha küçük ve modüler parçalara ayırmaya yardımcı olur. Program büyüdükçe fonksiyonlar, yazılan kodun
daha düzenli ve yönetilebilir hale gelmesinde büyük rol oynamaktadır. Kod tekrarını önleyerek, kodun
yeniden kullanılabilir hale getirilmesini sağlar.
Fonksiyon gibi bir tanımlama yapılmak istendiğinde def anahtar kelimesi kullanılmaktadır.
'''


def function_name():
    """docstring"""
    return print("hello world")


'''
Yukarıdaki fonksiyon tanımındaki deyimleri şu şekilde açıklayabiliriz:
def: Fonksiyon başlığının başlangıcını işaretleyen anahtar sözcüktür.
fonksiyon_adı: Fonksiyonu benzersiz şekilde tanımlamak için kullanılan bir tanımlamadır. Fonksiyon 
isimlendirme, Python’da değişken isimlendirme ile aynı kuralları izler.
parametre(ler): Bir fonksiyona iletmek istediğimiz değerlerdir. İsteğe bağlı olarak kullanılır.
İki nokta üst üste (:): Fonksiyon başlığının sonunu işaretlemek için kullanılır.
docstring (Yorum satırı): Fonksiyonun parametreleri ve fonksiyonun görevini açıklamak için isteğe 
bağlı yazılan açıklamaları içerir.
kod bloğu: Fonksiyon gövdesini oluşturan bir veya daha fazla geçerli python ifadesine verilen isimdir. 
İfadeler aynı girinti düzeyine sahip olmalıdır (genellikle 4 boşluk veya 1 tab girintisi).
return: Fonksiyondan bir değer döndürmek için isteğe bağlı olarak kullanılabilen bir dönüş ifadesidir.
'''


def greeting(name):
    """
    Bu fonksiyon, parametre olarak girilen kişiye selam verir
    """
    print("Merhaba, " + name + ". Günaydın!")


name = input("Lütfen isminizi giriniz:")
greeting(name)


def mutlak_deger(sayı):
    """Bu fonksiyon girilen sayının mutlak değerini döndürür """
    if sayı >= 0:
        return sayı
    else:
        return -sayı


print(mutlak_deger(11))
print(mutlak_deger(-26))


def deneme_fonk():
    x = 26

    print("Fonksiyon içindeki x değeri:", x)


x = 34
deneme_fonk()
print("Fonksiyon dışındaki x değeri:", x)
