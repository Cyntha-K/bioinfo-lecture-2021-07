with open("sequence.fasta", "r") as handle:
    for line in handle:
        line = line.strip()
        if line == "":
            continue
        print(line)
