print(range(10))
# 0-10 arası sayılar (10 hariç)
print(list(range(10)))
# 3-9 arası sayılar (9 hariç)
print(list(range(3, 9)))
# 3-19 arasındaki sayılar (19 hariç) 2 artarak
print(list(range(3, 19, 2)))


type = [ "Türk Pop", "Türkçe Rock", "Anadolu Rock", "Arabesk" ]

# liste üzerinde indis kullanarak ilerleyelim
for i in range( len( type ) ):
    print( type[i],"müziğini severim" )