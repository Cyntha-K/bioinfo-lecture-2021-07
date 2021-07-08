with open("sequence.protein.gb", "r") as handle:
    seq_list = list()
    for line in handle:
        line = line.strip()
        if line == "":
            continue
        else:
            seq_list.append(line)

title = seq_list[0]

print("title: ", title)

seq = "".join(seq_list)
seq = seq[seq.find("ORIGIN") + 6 :]

a = [i for i in seq if i.isalpha()]
a = "".join(a)

print("seq: ", a)
