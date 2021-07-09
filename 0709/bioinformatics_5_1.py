with open("sequence.nucleotide.fasta", "r") as handle:
    seq_list = list()
    for line in handle:
        line = line.strip()
        if line == "":
            continue
        elif line[0] != ">":
            seq_list.append(line)

seq = "".join(seq_list)

l_seq = list()
for i in range(0, len(seq) - 2, 3):
    print(i)
    l_seq.append(seq[i : i + 3])

for elem in l_seq:
    print(elem)
