'''Ad alanı, aynı amaç için oluşturulmuş sınıflar, fonksiyonlar ve özellikleri bir çatı altında toplayan yapıya verilen isimdir.
Namespace içerisine birbiri ile alakalı sınıf ve fonksiyonların konulmasına dikkat
edilmesi gerekir. Böylece aynı namespace içinde toplanan fonksiyonlar, ihtiyaç duyulan noktada koda
eklenerek daha kolay yönetilebilir kod yazmada yardımcı olmaktadır.'''

'''
Farklı ad alanları belirli bir zamanda bir 
arada bulunabilir ancak birbirinden tamamen 
yalıtılmış şekildedirler. Yani ad çakışmalarının 
olmaması sağlanmaktadır. Python yorumlayıcısını başlattığımızda tüm yerleşik, yani 
Python içerisinde ön tanımlı olarak gelen adları içeren bir ad alanı oluşturulur 
ve yorumlayıcı çalıştığı sürece varlığını devam ettirir. 
Böylece id(), print() vb. gibi yerleşik işlevler 
programın herhangi bir bölümünden her zaman kullanılabilir şekilde bulunmaktadır. 
Her modül kendi global ve yalıtılmış ad 
alanını oluşturmaktadır. Böylece farklı modüllerde bulunabilecek aynı isim çakışmasının 
önüne geçilmektedir. 
Modüllerin çeşitli işlevleri ve sınıfları olabilir. Bir işlev çağrıldığında, içinde tanımlanan 
tüm adlara sahip yerel bir ad alanı oluşturulur. 
Sınıflarda da benzer bir durum vardır.
'''

'''
Python Değişken Kapsamı (Scope)
Program içinde tanımlanmış bir değişkenin erişilebilir olduğu alan için kullanılan bir kavramdır. 
Tanımlanmış çeşitli ad alanları olmasına rağmen, programın her bölümünden hepsine erişilemeyebilir. 
Bu durumda kapsam (scope) kavramı devreye girmektedir.'''


def dis_fonk():
    b = 20

    def ic_fonk():
        c = 30


a = 10

print("========================")


def dis_fonksiyon():
    a = 20

    def ic_fonksiyon():
        a = 30
        print('a =', a)

    ic_fonksiyon()
    print('a =', a)


a = 10
dis_fonksiyon()
print('a =', a)

# a = 30
# a = 20
# a = 10

'''Kodun ekran çıktısından da görüldüğü gibi, 3 farklı “a” değişkeni farklı ad alanlarında tanımlanmış ve bu 
şekilde erişilmiştir. Aynı örneği a değişkeni için “global” anahtar kelimesini kullanarak tekrar inceleyelim.
'''

print("========================")


def dis_fonksiyon():
    global a
    a = 20

    def ic_fonksiyon():
        global a
        a = 30
        print('a =', a)

    ic_fonksiyon()
    print('a =', a)


a = 10
dis_fonksiyon()
print('a =', a)





