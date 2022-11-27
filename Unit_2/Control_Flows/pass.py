'''pass Deyimi
Türkçe karşılığı geçmek, sırasını atlatmak anlamına gelen pass deyimi, kodlamada da anlamına uygun şekilde kullanılmaktadır. Kod içinde kullanıldığında görmezden gel, hiç bir şey yapma gibi bir görev
üstlenir. Python’da bir yorum ve pass deyimi arasındaki farkı, yorumlayıcının bir yorumu tamamen yok
sayarken, pass deyimini yok saymamasıdır diyebiliriz. Pass deyimi genellikle bir işlevi olmaması gereken
fakat sözdizimi olarak bir ifade eklenmesi gereken durumlarda kullanılır.'''

'''pass daha sonra eklenecek işlemler için sadece bir yer tutucudur '''
metin = {'p', 'a', 's', 's'}
for harf in metin:
    pass

'''Kod örneğinde de görüldüğü gibi, pass ifadesini genelde yer tutucu olarak kullanırız. Henüz işlevi 
tanımlanmamış bir döngü veya fonksiyonumuz olduğunu ve bunu ileride hazırlamak istediğimizi varsayalım. Döngümüz boş bir kod bloğu ile tanımlandığında yorumlayıcı hata verecektir. Bu nedenle, hiçbir 
işlevi olmayan bir kod bloğu oluşturmak için pass ifadesini kullanılır. pass deyimi, aynı şekilde fonksiyon 
ve sınıflarda da kullanılabilir.'''


def function(parametre):


    pass


class DenemeSinifi:


    pass
