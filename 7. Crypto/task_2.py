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
def caesar_cipher(text: str, shift, mode: str = 'encrypt') -> str:
    result = ""
    for i in text:
        for j in i:
            if "a" <= j.lower() <= "z":
                if mode == "encrypt":
                    a = ((ord(j.lower()) - ord("a")) + shift) % 26
                else:
                    a = ((ord(j.lower()) - ord("a")) - shift) % 26
                s = (chr(a + ord("a")))
                result += s
            else:
                result += j
    return "".join(result)

print(caesar_cipher("Hello", 3, 'encrypt'))  # Должно вернуть: "Khoor"
print(caesar_cipher("Khoor", 3, 'decrypt'))  # Должно вернуть: "Hello"
print(caesar_cipher("XYZ", 5, 'encrypt'))  # Должно вернуть: "CDE" (циклический сдвиг)
print(caesar_cipher("Hello, World!", 13, 'encrypt'))  # Должно вернуть: "Uryyb, Jbeyq!"
