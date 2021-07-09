f1 = input("Enter input file: ")
f2 = input("Enter output file: ")

option1 = "Option-1) Read a FASTA format DNA sequene file and make a reverse sequence file."
option2 = "Option-2) Read a FASTA format DNA sequence file and make a reverse complement sequence file."
option3 = "Option-3) Convert GenBank format file to FASTA format file."

print(option1)
print(option2)
print(option3)

select = input("Select the option: ")

if select == "1":
    with open(f"{f1}", "r") as handle:
        seq_list = list()
        for line in handle:
            line = line.strip()
            if line == "":
                continue
            elif line.startswith(">"):
                continue
            else:
                seq_list.append(line)

    seq = "".join(seq_list)

    f = open(f"{f2}", "w")
    f.close()

    with open(f"{f2}", "w") as data:
        data.write(seq[::-1])

elif select == "2":
    with open(f"{f1}", "r") as handle:
        seq_list = list()
        for line in handle:
            line = line.strip()
            if line == "":
                continue
            elif line.startswith(">"):
                continue
            else:
                seq_list.append(line)

    seq = "".join(seq_list)

    with open(f"{f2}", "w") as data:
        seq = seq.lower()
        seq = seq.replace("a", "T")
        seq = seq.replace("c", "G")
        seq = seq.replace("g", "C")
        seq = seq.replace("t", "A")

        data.write(seq[::-1])


elif select == "3":
    with open(f"{f1}", "r") as handle:
        seq_list = list()
        for line in handle:
            line = line.strip()
            if line == "":
                continue
            else:
                seq_list.append(line)
    title = seq_list[0]

    seq = "".join(seq_list)
    seq = seq[seq.find("ORIGIN1") + 7 :]

    a = [i for i in seq if i.isalpha()]
    a = "".join(a)

    sequence = ">" + title + "\n" + a

    with open(f"{f2}", "w") as data:
        data.write(sequence)

else:
    print("sorry")
