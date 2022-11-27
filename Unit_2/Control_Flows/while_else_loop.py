'''while…else Döngüsü
for döngüsünde olduğu gibi, while döngüsünde de isteğe bağlı bir else bloğu kullanılabilir.
while döngüsündeki koşul Yanlış (False) olarak değerlendirilirse, else kısmı yürütülür.
Ayrıca while döngüsü bir break deyimi ile sonlandırılabilir.
Bu gibi durumlarda, else kısmı göz ardı edilir. Bu nedenle, bir while
döngüsünün else kısmı, while bloğundaki kodda herhangi bir kesinti olmazsa ve
while test koşulu yanlış (False) ise, yani while döngüsü doğal şekilde
tamamlandıysa çalışacaktır. Bir örnek ile inceleyelim.'''

counter=0

while counter<=5:
    print("while bloğu içinde, sayac", counter)
    counter=counter+1
else:
    print("else bloğu içinde")

