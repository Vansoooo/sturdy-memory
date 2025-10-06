a = input()
s = []
for i in a:
    s.append(int(i))
result = [str(int(i)**2) for i in s]
print(''.join(result))