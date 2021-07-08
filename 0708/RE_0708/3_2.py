with open("../sequence.fasta", "r") as handle:
    for line in handle:
        line = line.strip()
        break

print(f"The first line is: {line}")
