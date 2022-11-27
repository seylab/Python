# 1 den kullanıcının girdiği n sayısına kadar
# doğal sayıların toplanması işlemi
# toplam = 1+2+3+...+n

# Kullanıcıdan girdi alınması
n=int(input("n değerini giriniz: "))

# toplamı ve sayacı başlat
total= 0
counter=1

while counter<= n:
    total=total+counter
    counter=counter+1

# toplam değerinin yazdırılması
print("Toplam", total)
