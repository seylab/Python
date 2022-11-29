import math

print("Pi: ", math.pi)
print("6!: ", math.factorial(6))
print("Sin(1) : ", math.sin(1))
print("Sinh(1): ", math.sinh(1))
print("Cos(Pi): ", math.cos(math.pi))
print("e^100: ", math.exp(100))
print("Log(10000): ", math.log10(10000))

import random

# 5 ile 30 arasında rastgele bir tamsayı değer döndürür
print(random.randrange(5, 30))

dizi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# Dizi den rastgele bir değer döndürür
print(random.choice(dizi))

# Diziyi karışık şekilde dizer
random.shuffle(dizi)

# Karıştırılmış diziyi ekrana yazar
print(dizi)

# Rastgele bir değer döndürür
print(random.random())
