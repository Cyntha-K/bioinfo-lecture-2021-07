#! /usr/bin/python3

num = input('num?')

while not num.isdigit():
     num = input('number?')

num = int(num)

if num % 3 == 0:
    result = '3의 배수'
elif num % 7 == 0:
    result = '7의 배수'
else:
    result = 'none'

print(result)

