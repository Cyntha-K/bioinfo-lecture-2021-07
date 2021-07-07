with open("061.fastq", "r") as handle:
    read_count = len(handle.readlines()) / 4
print(read_count)


with open("061.fastq", "r") as data:
    for line in data:
        read_line = handle.readline()
    print(read_line)
