import sys

try:
    val = int(input("enter: "))
except ValueError as err: 
    print(err)
    sys.exit()


try:
    print(10/val)
except ZeroDivisionError as err1:
    print(err1)
    sys.exit(1)




import sys

val = int(input("enter: "))

try: 
    print(10/val)
except ValueError as err1:
    print(err)
    sys.exit()
except ZeroDivisionError as err2:
    print(err2)
    sys.exit()

