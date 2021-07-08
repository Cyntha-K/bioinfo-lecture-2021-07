num = input("Which times table: ")

while not num.isdigit():
    num = input("please input number!")

num = int(num)

if 0 < num < 10:
    for i in range(1, 10):
        print(f"{num} * {i} = ", num * i)
else:
    print("What?")
