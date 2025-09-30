def tetration(number, degree):
    s = 1
    for i in range(degree):
        s = number * s
    return number**s
print(len(str(tetration(5,3))), len(str(tetration(2,5))))
