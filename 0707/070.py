count = 0

with open("070.vcf", "r") as handle:
    for line in handle:
        data = line.strip().split("\t")
        if line.startswith("##"):
            continue

        # print(read_count)
        if data[6] == "PASS":
            count += 1
        read_count = handle.readlines()

print(read_count)
print(count)
