a = [input() for i in range(4)]
print(a)
b = [input() for i in range(2)]
print(b)
result = []
for x in a:
    if x not in b:
        result.append(x)
print(result)