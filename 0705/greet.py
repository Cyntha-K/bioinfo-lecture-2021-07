#! /usr/bin/python3

def greet():
    print("Hello")

def greet1(name: str) -> None:
    print(f"hello, {name}")
 
def greet2(num: int) -> int:
    return num * 2



greet()
ret1 = greet1("ken")
print(ret1)

ret2 = greet2(3)
print(ret2)


