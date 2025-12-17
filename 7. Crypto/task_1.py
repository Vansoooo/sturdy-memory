n = input()
def in_cod(n):
    word = []
    asc = []
    word.append(n)
    for i in word:
        for j in i:
            a = ord(j)+3
            asc.append(chr(a))
    return asc
def out_cod(n):
    word = []
    asc = []
    word.append(n)
    for i in word:
        for j in i:
            a = ord(j)-3
            asc.append(chr(a))
    return asc
print(in_cod(n))
print(out_cod(in_cod(n)))
