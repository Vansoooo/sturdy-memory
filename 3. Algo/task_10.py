from itertools import *
result = []
for n in permutations("0123456789"):
    if (int(n[1] + n[2] + n[3]) % 2 and int(n[2] + n[3] + n[4]) % 3 \
        and int(n[3] + n[4] + n[5]) % 5 and int(n[4] + n[5] + n[6]) % 7 \
        and int(n[5] + n[6] + n[7]) % 11 and int(n[6] + n[7] + n[8]) % 13 \
        and int(n[7] + n[8] + n[9]) % 17 == 0):
        result.append(int(''.join(n)))
print(sum(result))