#! /usr/bin/python3


import sys
 
if len(sys.argv) != 3:
    print(f"#usafe: python {sys.argv[0]} [n1] [n2]")
    sys.exit

n1 = int(sys.argv[1])
n1 = int(sys.argv[2])

print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")
print(f"{n1} / {n2} = {n1 / n2}")
print(f"{n1} ** {n2} = {n1 ** n2}")
