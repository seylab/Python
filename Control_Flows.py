# Sayı pozitif ise uygun bir mesaj yazdırıyoruz

sayı = 3
if sayı > 0 :
    print(sayı, "pozitif bir sayıdır.")
print("Bu her zaman yazdırılır.")


sayı = -1
if sayı > 0 :
    print(sayı, "pozitif bir sayıdır.")
print("Bu da her zaman yazdırılır.")

# sayının pozitif mi negatif mi olduğunu kontrol ederek
# uygun mesajı verelim
sayı = 7
# Bu iki değeri sırayla vererek test edin
# sayı = 0
# sayı = -9
if sayı >= 0 :
    print("Pozitif veya Sıfır")
else:
    print("Negatif sayı")



''' Sayının pozitif, negatif veya sıfır olup olmadığını kontrol ederek 
uygun bir mesaj gösterelim '''

sayı = 2.54
# Bu iki farklı değeri de deneyelim:
# sayı = -56.3
# sayı = 0

if sayı > 0:
    print("Pozitif sayı")
elif sayı == 0:
    print("Sıfır")
else:
    print("Negatif sayı")
   
''' 
Bu sefer iç içe if ifadesini kullanarak, kullanıcının girdiği sayının pozitif, 
negatif veya sıfır olup olmadığını kontrol edelim ve uygun bir mesaj gösterelim
'''
sayı = float(input("Bir sayı giriniz: "))
if sayı >= 0 :
    if sayı == 0:
        print("Sıfır")
    else:
        print("Pozitif sayı")
else:
    print("Negatif sayı")

    