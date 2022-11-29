import fractions as F

print(F.Fraction(2.5))
print(F.Fraction(5))
print(F.Fraction(4, 3))

# Float olarak kullanım
print(F.Fraction(2.2))
# Metin dizesi olarak kullanım
print(F.Fraction('2.2'))

print("====================================")

from fractions import Fraction as F

print(F(2, 3) + F(3, 3))
print(1 / F(3, 7))
print(F(-5, 9) > 0)
print(F(-5, 9) < 0)
