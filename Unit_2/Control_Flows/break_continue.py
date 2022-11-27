'''
break ifadesi, onu içeren döngüyü sonlandırmak için
kullanılır. Programın çalışma sırası, döngünün gövdesinden
hemen sonraki ifadeye geçer. break ifadesi iç içe bir döngü
içinde ise (döngü başka bir döngü içinde ise), break ifadesi
en içteki döngüyü sonlandıracaktır.
'''

for harf in "Python Öğreniyorum":
    if harf == "o":
        break
    print(harf)
print("for bloğundan sonra")

sayac = 1

while sayac < 10:
    if sayac % 4 == 0:
        break
    print(sayac)
    sayac = sayac + 1
print("while bloğundan sonra")

'''
Türkçe karşılığı devam anlamına gelen continue deyimi, bir döngü içindeyken kendisinden sonraki 
kodları çalıştırmadan, döngünün başına gelerek işleme bir sonraki eleman ile devam edilmesini sağlar. Yani 
break deyimindeki gibi döngü sonlandırılmaz, ancak bir sonraki döngü elemanı ile devam eder.
'''
for num in range(13):
    if num % 3 == 0:
        continue
    print(num)

    '''Örnek kodda sayı 3 ile tam bölünebiliyorsa yorumlayıcı continue deyimi ile kodun kalan kısmını es 
geçerek, döngünün başına gelmektedir.'''


