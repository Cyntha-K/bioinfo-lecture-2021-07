#! /usr/bin/python3

import math
import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]}[num]")
    sys.exit 

a = int(sys.argv[1])

pi = math.pi

result = round(a**2*pi, 2)

print(result)
