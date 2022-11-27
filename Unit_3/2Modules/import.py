import matematik

print(matematik.carp(3, 5))

print("=========================================")

# import (içe aktarma) ifadesi örneği
# standart math (matematik) modülü içe aktarma
import math

print("Pi sabiti değeri:", math.pi)

print("=========================================")

# yeniden isimlendirme ile modülün içe aktarımı
import math as m

print("Pi sabiti değeri:", m.pi)
print("5! değeri:", m.factorial(5))

print("=========================================")

# math modülünden sadece karekök almaya yarayan sqrt fonksiyonunu alalım
from math import sqrt

print("256 sayısının karekökü:", sqrt(256))

print("=========================================")

from math import pi, e, sqrt as karekok

print(pi)

print(e)

print(karekok(25))

print("=========================================")

from math import *

print("Pi sabiti değeri:", pi)
print("25 sayısının karekökü:", sqrt(25))



print("=========================================")
import math

print(math.__init__)
