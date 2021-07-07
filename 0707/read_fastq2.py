cnt = 0
data = dict()

with open("061.fastq", "r") as handle:
    for line in handle:
        if cnt % 4 == 0:  # header
            pass
        elif cnt % 4 == 1:  # base
            for base in line.strip():
                if base not in data:
                    data[base] = 0
                data[base] += 1
        elif cnt % 4 == 2:  # delimiter
            pass
        elif cnt % 4 == 3:  # quality
            pass
        cnt += 1


print(data)
print(cnt / 4)
