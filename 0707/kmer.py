num = input("number?")

base_data = ["A", "T", "G", "C"]


def kmer(base):
    base += base
    return base


for i in range(num):
    for base in base_data:
        kmer(base)
    print(kmer)

print(f"{num}mer: ", kmer)
