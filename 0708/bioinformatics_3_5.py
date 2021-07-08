with open("sequence.protein.2.fasta", "r") as handle:
    count = 0
    for line in handle:
        line = line.strip()
        if count == 1:
            break
        count += 1

print(f"The second line is: {line}")
