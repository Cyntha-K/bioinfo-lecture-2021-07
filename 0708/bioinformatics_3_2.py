fr = open("title.txt", "r")
lines = fr.readlines()
for line in lines:
    line = line.strip()
    break
fr.close()

print(f"The first line is : {line}")
