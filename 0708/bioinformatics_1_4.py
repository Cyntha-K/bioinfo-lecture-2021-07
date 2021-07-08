num1 = input("Enter a integer: ")
num2 = input("Enter another: ")

num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num2 > num1:
    print(f"{num1} is less than {num2}.")
else:
    print(f"{num1} is equal to {num2}.")
