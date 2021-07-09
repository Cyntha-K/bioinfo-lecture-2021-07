with open("sequence.nucleotide.gb", "r") as handle:
    seq_list = list()
    for line in handle:
        if line == "":
            continue
        else:
            seq_list.append(line)

seq = "".join(seq_list)

seq_position = list()
seq_position2 = list()
index = -1
index2 = -1

while True:
    index = seq.find("TITLE", index + 1)
    index2 = seq.find("JOURNAL", index2 + 1)
    if index == -1 & index2 == -1:
        break
    position = index + 1
    position2 = index2 + 1

    seq_position.append(position)
    seq_position2.append(position2)

    print(seq_position)
    print(seq_position2)

    seq_lis = list()

    for i in seq_position:
        for r in seq_position2:
            sequence = seq[i:r]
            seq_lis.append(sequence)

    seq_l = "".join(seq_lis)
    print(seq_l)
