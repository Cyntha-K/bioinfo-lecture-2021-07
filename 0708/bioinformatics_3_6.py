with open("sequence.protein.2.fasta", "r") as handle:
    title = ""
    seq_list = list()
    for line in handle:
        line = line.strip()
        if line == "":
            continue
        if line[0] != ">":
            seq_list.append(line)
        else:
            title = line

seq = "".join(seq_list)
print(f"title: {title}")
print(f"seq: {seq}")
