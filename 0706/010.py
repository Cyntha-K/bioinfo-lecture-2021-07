def my_sum(a,b):
    result = a + b
    return result

a = input('number1?')
b = input('number2?')

while not (a.isdigit() & b.isdigit()):
    a = input('number1?')
    b = input('number2?')

a = int(a)
b = int(b)

print(my_sum(a, b))
 

