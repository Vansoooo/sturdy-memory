print("начальный день")
n = int(input())
print("сколько дней в месяце")
k = int(input())
day = 1
for i in range(1,n-1):
    print("   ",end="")
i = n
while k >= day:
    if day <= 10:
        print(f" {day}",end="")
    else:
        print(f"{day}", end="")
    if i % 7 == 0 or n == k:
        print()
    else:
        print(" ", end="")
    day += 1
    i += 1