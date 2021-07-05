#! /usr/bin/python3

num = input('num?')

while not num.isdigit():
    num = input('input number')
num = int(num)

if num % 2 == 0:
    print('even')
else:
    print('odd')


