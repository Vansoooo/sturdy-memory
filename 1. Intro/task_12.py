a = int(input())
c = input("Перевести в байты (1) или килобайты (2): ")
def kb(n):
    s = n / 1024
    return s
def b(n):
    s = n * 1024
    return s
if c == "1":
    print("kb = ",a,"b = ",b(a))
if c == "2":
    print("b = ", a, "kb = ", kb(a))