#! /usr/bin/python3


nb = input('calculate? press enter!')
num0 = input('number?')
num1 = input('number?')
op = input('operator?')

operator = {'+', '-', '*', '/'}

while not num0.isdigit() & num1.isdigit() & operator.issuperset(op): 
    nb = input('calculate? press enter!')
    num0 = input('number?')
    num1 = input('number?')
    op = input('operator?')

num0 = int(num0)
num1 = int(num1)

def calc(num0, num1, op):
    if op == '+' :
        result = num0 + num1 
    elif op == '-':
        result = num0 - num1 
    elif op == '*' :
        result = num0 * num1
    elif op == '/' :
        result = num0 / num1
    else:   
        result = 'so hard..'
    return result
    
result = calc(num0, num1, op)

print(result)
