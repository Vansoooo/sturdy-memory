def f(month):
    if month == 2:
        return 28
    if month in [4,6,9,11]:
        return 30
    else:
        return 31

a = int(input("Введите номер месяца: "))
b = int(input("Введите год: "))
c = f(a)
print(c)
