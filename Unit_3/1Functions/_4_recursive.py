def faktöriyel(x):
    """ Bu özyinelemeli fonksiyon, verilen bir tamsayının
    faktöriyel değerini bulmak için hazırlanmıştır """
    if x == 1:
        return 1
    else:
        return (x * faktöriyel(x - 1))


sayi = 5
print(sayi, "sayısının faktöriyel değeri: ", faktöriyel(sayi))
