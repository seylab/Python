'''Global variables'''

x = "global"


def degisken_test():
    print("x fonksiyon içinde:", x)


degisken_test()
print("x fonksiyon dışında:", x)

print("==============")


def dis_fonk():
    x = 20

    def ic_fonk():
        global x
        x = 25

    print("İç fonksiyon çağrısından önce x:", x)
    ic_fonk()
    print("İç fonksiyon çağrısından sonra x:", x)


dis_fonk()
print("Ana kod bloğunda x:", x)

print("=========================================")


def test():
    x = "local değişken"
    print(x)


test()

print("=========================================")

x = "global değişken "


def test():
    global x
    y = "local değişken"
    x = x * 2
    print(x)
    print(y)


test()

print("=========================================")

x = 22


def test():
    x = 34
    print("local x:", x)


test()
print("global x:", x)

print("=========================================")


def dis_fonksiyon():
    x = "local"

    def ic_fonksiyon():
        nonlocal x
        x = "nonlocal"
        print("iç fonksiyon:", x)

    ic_fonksiyon()
    print("dış fonksiyon:", x)


dis_fonksiyon()

print("=========================================")
