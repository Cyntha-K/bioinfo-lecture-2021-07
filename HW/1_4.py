import sys

num = input('n?')
try:
    num = int(num)
    print(10/num)
except ValueError as err1:
    print(err1)
except ZeroDivisionError as err2:
    print(err2)

