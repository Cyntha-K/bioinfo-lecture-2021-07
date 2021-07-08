with open("sequence.fasta", "r") as handle:
    seq_list = list()
    for line in handle:
        line = line.strip()
        if line == "":
            continue
        seq_list.append(line)

seq = "\n".join(seq_list)

fw = open("sequence.protein.2.fasta", "w")
fw.write(seq)
fw.close()
