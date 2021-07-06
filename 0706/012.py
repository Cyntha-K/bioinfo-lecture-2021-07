def Factorial(a):
    result = 1
    num = a

    while num > 0:
        result *= num
        num -= 1

    return result

a = input('number?')

while not a.isdigit():
    a = input('again')

a = int(a)

result = Factorial(a)




print(result)
