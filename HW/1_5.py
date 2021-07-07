import sys

i = int(sys.argv[1])

def facto(i):
    for r in range(0, i):
        if r == 0: 
            result = 1
        elif r == 1:
            result = 1
        else:
            result = r * int(facto(r-1))
            r += 1


print(facto(i))
