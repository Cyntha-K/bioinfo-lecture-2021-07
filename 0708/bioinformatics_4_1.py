with open("sequence.protein.gb", "r") as handle:
    for line in handle:
        seq_list = list()
        line = line.strip()
        if line == "":
            continue
        if line[0] == "ORIGIN":
            seq_list.append(line)
seq = "".join(seq_list)

print(seq)
