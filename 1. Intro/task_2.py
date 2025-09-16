print("введите расстояние в киломатрах")
a = int(input())
print("введите расстояние в метрах")
b = int(input())
c = a*1000
if c<b:
    print(c)
else:
    print(b)