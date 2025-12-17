def rot13(n):
    word = []
    word.append(n)
    result = ""
    for i in word:
        for j in i:
            if "a" <= j.lower() <= "z":
                a = ((ord(j.lower()) - ord("a"))+13)%26
                s = (chr(a + ord("a")))
                result += s
            else:
                result += j
    return "".join(result)
print(rot13("Uryyb, Jbeyq!"))        # Должно вернуть: "Hello, World!"
print(rot13(rot13("Test")))          # Должно вернуть: "Test"
print(rot13("123!@#"))
