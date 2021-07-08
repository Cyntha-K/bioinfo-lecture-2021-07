codon_dic = dict()

while True:
    codon = input("Enter three-base codon to build: ")
    codon = codon.upper()
    if codon == "XXX":
        print("Okay, I will switch.")
        break
    aa = input("Enter amino acid: ")
    aa = aa.upper()
    codon_dic[codon] = aa

while True:
    codon = input("Enter three-base codon to search: ")
    codon = codon.upper()
    if codon == "XXX":
        print("Okay, I will stop.")
        break
    if codon in codon_dic:
        aa = codon_dic[codon]
        print("Amino acid for %s: %s" % (codon, aa))
    else:
        print("%s codon does not exist." % (codon))
