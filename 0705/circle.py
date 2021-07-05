#! /usr/bin/env python

radius = input('radius?')

while not radius.isdigit():
    radius = input('reinput radius: ')

radius = int(radius)

def area(r):
    result = r * r * 3.141592
    return result

area = area(radius)

print(area)



