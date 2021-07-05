#! /usr/bin/python3

#solution1 

nb = input('number: ')

if nb.isdigit():
    nb = int(nb)
    for i in range(2, 10, 2):
        result  = nb * i 
        print(result)
else:
    import sys
    sys.exit('sorry')
