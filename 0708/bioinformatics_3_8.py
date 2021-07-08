with open("sequence.protein.2.fasta", "r") as handle:
    for line in handle:
        title = ""
        seq_list = list()
        line = line.strip()
        if line == "":
            continue
        if line[0] != ">":
            seq_list.append(line)
        else:
            title = line

seq = "".join(seq_list)

while True:
    amino = input("Searching for: ")
    if amino == "XXX":
        print("Okay, I will stop.")
        break
    else:
        index = -1
        while True:
            index = seq.find(amino, index + 1)
            if index == -1:
                break
            print(f"Found at: {index}")
