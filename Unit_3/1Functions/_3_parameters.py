def selamlama(isim, mesaj):
    """
    Bu fonksiyon, parametre olarak girilen isme, yine parametre
    olarak verilen mesajı verir
    """
    print("Merhaba " + isim + ", " + mesaj)


isim = input("Lütfen isminizi giriniz: ")
mesaj = input("Lütfen mesajı giriniz: ")
selamlama(isim, mesaj)


def selamlama(isim, mesaj="Sitemizi ziyaret ettiğiniz için teşekkür ederiz"):
    """
    Bu fonksiyon, parametre olarak girilen isme, yine parametre
    olarak verilen mesajı verir
    """
    print("Merhaba " + isim + ", " + mesaj)


isim = input("Lütfen isminizi giriniz: ")
selamlama(isim)
selamlama(isim, "Herkese benden çay!")

@Test
def selamlama(*isimler):
    """
    Bu fonksiyon, parametre olarak verilen isimlerdeki tüm kişileri
    selamlar
    """
    for isim in isimler:
        print("Merhaba " + isim)


selamlama("Harun", "Kerem", "Nurullah", "Mustafa", "Orkun")
