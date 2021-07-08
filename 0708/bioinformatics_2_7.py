d_base = {}

for len(list(d_base.keys())) in range(65):

    base = input("Enter three base codon to build: ")
    amino = input("Enter amino acid: ")

    while not (base.isalpha() & amino.isalpha()):
        base = input("Enter three-base codon to build: ")
        amino = input("Enter amino acid: ")

    base = base.upper()
    amino = amino.upper()


    if base == "XXX":
        print("Okay, I will switch.")
        

        if not base in d_base.keys():
            print("I dont know")
        else:
            print(d_base[f"{base}"])

