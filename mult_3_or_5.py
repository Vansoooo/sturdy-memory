def f(n):
    summ = 0
    if n <= 0:
        return 0
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0:
            summ += i
    return summ
print(f(10))