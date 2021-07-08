with open("sequence.protein.2.fasta", "r") as handle:
    seq_list = list()
    for line in handle:
        title = ""

        line = line.strip()
        if line == "":
            continue
        if line[0] != ">":
            seq_list.append(line)
        else:
            title = line

seq = "".join(seq_list)

# print(seq)

while True:
    amino = input("Searching for: ")
    if amino == "XXX":
        print("Okay, I will stop.")
        break
    else:
        l_position = []
        index = -1
        while True:
            index = seq.find(amino, index + 1)
            if index == -1:
                break
            position = index + 1

            l_position.append(position)

        print(f"Found at: {l_position}")
