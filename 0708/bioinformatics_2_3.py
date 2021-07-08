s = input("Enter a string: ")
num = input("How many times to repeat: ")

# print(s.replace(" ", ""))

while not (s.replace(" ", "").replace(".", "").isalpha() & num.isdigit()):
    s = input("Reenter a string: ")
    num = input("How many times to repeat: ")

num = int(num)

print(s * num)
