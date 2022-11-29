# Python'da string tanımlama
# Aşağıdaki tanımlamaların hepsi eşdeğerdir
metin_dizisi = 'Merhaba'
print(metin_dizisi)
metin_dizisi = "Merhaba"
print(metin_dizisi)
metin_dizisi = '''Merhaba'''
print(metin_dizisi)
# Metin, üçlü tırnak dizisi ile birden çok satıra uzatılabilir
metin_dizisi = """Merhaba, Python dünyasına 
 hoş geldiniz"""
print(metin_dizisi)

str = 'Anadolu Üniversitesi'
print('str = ', str)
# ilk karakter
print('str[0] = ', str[0])
# son karakter
print('str[-1] = ', str[-1])
# 3. ila 7. karakter arasını dilimleme
print('str[3:7] = ', str[3:7])
# 7. karakterden sondan 2. karaktere kadar dilimleme
print('str[7:-2] = ', str[7:-2])

# Python String İşlemleri
str1 = 'Merhaba '
str2 = 'Python!'
# + operatörü kullanılarak
print('str1 + str2 = ', str1 + str2)
# metinler yan yana yazılarak
print('Merhaba ' 'Python!')
print('Merhaba '
      'Python!')
# * operatörü kullanılarak
print('str1 * 3 =', str1 * 3)

# dize üzerinde yineleme
sayac = 0
for harf in 'Açıköğretim Fakültesi':
    if (harf == 'i'):
        sayac += 1
print(sayac, 'tane i harfi bulundu')

var = 'a' in 'Osmangazi'
print(var)

var = 'un' not in 'Orhun'
print(var)

var = 'ancak' in 'Sancaktepe'
print(var)

metin = 'Programlama'
# enumerate()
list_enumerate = list(enumerate(metin))
print('list(enumerate(metin) = ', list_enumerate)
# karakter sayısı
print('len(metin) = ', len(metin))

print('''Ani bastıran kar fırtınasının ortasında kalan Atlas, eşine "Toprak'ın elini sakın bırakma!" diye seslendi.''')
print('Ani bastıran kar fırtınasının ortasında kalan Atlas, eşine "Toprak\'ın elini sakın bırakma!" diye seslendi.')
print("Ani bastıran kar fırtınasının ortasında kalan Atlas, eşine \"Toprak'ın elini sakın bırakma!\" diye seslendi.")

######################################################
# \newline Ters bölü ve yeni satır yoksayıldı
# \\ Ters bölü
# \’ Tek alıntı
# \” Çift alıntı
# \a ASCII Çanı
# \b ASCII Geri silme
# \f ASCII Form beslemesi
# \n ASCII Satır beslemesi
# \r ASCII Satır başı
# \t ASCII Yatay sekmesi (tab)
# \v ASCII Dikey Sekmesi
# \ooo Sekizlik değeri ooo olan karakter
# \xHH Onaltılık değeri HH olan karakter

print("C:\\Program Files\\Python")
print("Bu metin\nüç satır\nşeklinde ekrana yazılacak")
print("Bu bir \x48\x45\x58 gösterimdir")

print("Bu, kaçış dizileri için \nçok farklı \x62\x69\x72 örnek olacak")
print(r"Bu, kaçış dizileri için \nçok farklı \x62\x69\x72 örnek olacak")

#############################################
# Python dize format() yöntemi
# varsayılan (örtük) sıralama
varsayılan_sıra = "{}, {} ve {}".format('Fahri', 'Emin', 'Musa')
print('\n--- Varsayılan Sıra ---')
print(varsayılan_sıra)
# konumsal argümanı kullanarak sıralama
konumsal_sıra = "{1}, {0} ve {2}".format('Fahri', 'Emin', 'Musa')
print('\n--- Konumsal Sıra ---')
print(konumsal_sıra)
# anahtar kelime argümanını kullanarak sıralama
anahtar_kelime_sıra = "{m}, {f} ve {e}".format(f='Fahri', e='Emin', m='Musa')
print('\n--- Anahtar Kelime Sırası ---')
print(anahtar_kelime_sıra)

############################################

# tam sayıları biçimlendirme
print("{0} öğesinin ikili gösterimi {0:b} şeklindedir".format(97))
# noktalı sayıları biçimlendirme
print("Üs temsili: {0:e}".format(1040.567))
# yuvarlama
print("Üçte biri: {0:.3f}".format(1 / 3))
# dize hizalama
print("|{:<10}|{:^10}|{:>10}|".format('peynir', 'tereyağı', 'ekmek'))

###############################################

x = 987.654321
print('x değeri %3.2f' % x)
print('x değeri %3.4f' % x)

###############################################

print("EsKiŞeHiR".lower())
print("EsKiŞeHiR".upper())
print("Bu, tüm kelimeleri bir listeye böler".split())
print(['Bu', 'ifade', 'tüm', 'kelimeleri', 'içine', 'alan', 'metindir.'])
print(' '.join(['Bu', 'ifade', 'tüm', 'kelimeleri', 'içine', 'alan', 'metindir.']))
print('Hayırlı Bayramlar'.find('ram'))
print('Hayırlı Mutlu Bayramlar'.replace('Mutlu', 'Parlak'))
