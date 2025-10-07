k = int(input())
def f(k1):
    k2 = k1 + 1
    n = 1
    while True:
        a = str(k1*n)
        b = str(k2*n)
        a_sort = sorted(a)
        b_sort = sorted(b)
        if a_sort == b_sort:
            return n
        n += 1
print(f(k))