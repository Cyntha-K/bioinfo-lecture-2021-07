length = []
with open("077.bed", "r") as handle:
    for line in handle:
        data = line.strip().split("\t")
        num1 = int(data[1])
        num2 = int(data[2])
        num = num2 - num1
        length.append(num)

print(sum(length))
