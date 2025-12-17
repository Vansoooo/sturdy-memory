def gaderypoluki(message: str, key: str, mode: str = "encode"):
    key = key.lower()
    s = {}
    for i in range(0, len(key),2):
        key1,key2 = key[i], key[i+1]
        s[key1] = key2
        s[key2] = key1
        s[key1.upper()] = key2.upper()
        s[key2.upper()] = key1.upper()
    result = "".join(s.get(i,i) for i in message)
    return result


print(gaderypoluki("ABCD", "agedyropulik","encode"))              #// => GBCE
print(gaderypoluki("Ala has a cat", "gaderypoluki","encode"))     #// => Gug hgs g cgt
print(gaderypoluki("Dkucr pu yhr ykbir","politykarenu","decode")) #// => Dance on the table
print(gaderypoluki("Hmdr nge brres","regulaminowy","decode"))     #// => Hide our beers
