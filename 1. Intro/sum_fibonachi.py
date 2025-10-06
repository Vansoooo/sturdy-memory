s = [1,2]
fib_list = []
i = 3
while max(s) <= (4*10**6):
    s.append(s[i-2] + s[i-3])
    i += 1
for i in s:
    if i % 2 == 0:
        fib_list.append(i)
result = sum(fib_list)
print(result)