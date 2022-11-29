x = 82
y = 7 + 5j
print(y + 3)
print(isinstance(y, complex))
print(type(x))
print(type(86.0))

# Binary (2 lik taban)          ‘0b’ veya ‘0B’
# Octal (8 lik taban)           ‘0o’ veya ‘0O’
# Hexadecimal (16 lık taban)    ‘0x’ veya ‘0X’

print("=================================")

print(0b10101011)
# 171
print(0xFB + 0b101)
# 256
print(0o25)
# 21


print("=================================")
#
print(2 + 7.0)
# 9.0

'''türler arasında açık bir şekilde dönüştürme yapmak için 
int(), float() ve complex() gibi hazır fonksiyonlar da kullanılabilir. Bu fonksiyonlar yardımıyla, karakter 
dizeleri de sayıya dönüştürülebilir'''

print("=================================")
print(int(12.26))
print(int(-9.26))
print(float(76))
print(complex('5+71j'))

import decimal

print(0.2)

print(decimal.Decimal(0.2))
