n = int(input())
k = int(input())
def f(n,k):
    factorial = 1
    for i in range(1,n):
        factorial = factorial * i
    s = k
    count = 0
    while factorial > s:
        count += n // s
        s = s * k
    return count
print(f(n,k))