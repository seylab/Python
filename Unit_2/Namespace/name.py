'''Python’da her şey bir nesnedir. Ad (tanımlayıcı olarak da adlandırılır) nesnelere verilen bir isimdir. Ad,
temel alınan nesneye erişmenin bir yoludur.
Örneğin, sayi = 10 atamasını yaptığımızda, 10 bellekte depolanan bir nesnedir ve “sayi”, onu ilişkilendirdiğimiz isimdir.
Python’un hazır fonksiyonlarından id() aracılığıyla bazı nesnelerin RAM’deki adresini
alabiliriz. Nasıl kullanılacağına bir örnek ile inceleyelim.'''


""" 
Not: id fonksiyonunu kendi bilgisayarınızdan çalıştırdığınızda, örnekte verilenden farklı hafıza değerleri getirebilir
"""
a = 20
print('id(20) =', id(20))
print('id(a) =', id(a))


'''Kod örneğimizde iki id fonksiyonu da 20 değerine eriştiği için aynı adres değerini elde ettik. Şimdi 
biraz daha farklı bir örnek ile id() fonskiyonunu inceleyelim. '''

""" 
Not: id fonksiyonunu kendi bilgisayarınızdan çalıştırdığınızda, örnektekinden 
farklı hafıza değerleri getirebilir
"""
a = 20
print('id(a) =', id(a))
a = a+10
print('id(a) =', id(a))
print('id(30) =', id(30))
b = 20
print('id(b) =', id(b))
print('id(20) =', id(20))

print("================")

a = 5
print( id(a) )
a = 'Merhaba Python kodlayanlar!'
print( id(a) )
a = [1,2,3]
print( id(a) )

def merhabaYaz():
    print("Merhaba!")
a = merhabaYaz
a()
print( id(a))