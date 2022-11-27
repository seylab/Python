'''switch-case Deyimi
Eğer kod içerisinde bir ifade için yapılması gereken kontrol işlemleri sayıca fazla ise, if..else blokları
yerine, C#, Java ve JavaScript gibi programlama dillerindeki switch deyimi kullanılabilir. Fakat diğer dillerin aksine, Python dilinde switch-case ifadesi bulunmamaktadır. Bu durumu aşmak için sözlük eşleşmesi
(dictionary mapping) kullanılmaktadır.'''


def trafik_isigi(argument):
    switcher = {
        1: "Kırmızı",
        2: "Sarı",
        3: "Yeşil",
    }

    return switcher.get(argument, "Bulunamadı...")

status = input("Trafik ışığı sırasını giriniz:")
print(trafik_isigi(int(status)))
