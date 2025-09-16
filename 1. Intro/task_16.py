a = int(input())
n = input().split()

b = [0]*(n+1)

for g in range(1,n+1):
    seat = int(n[g - 1])
    b[seat] = g
print(n)
print(b[1:])
