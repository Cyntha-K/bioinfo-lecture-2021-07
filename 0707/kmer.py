n = input("number?")

n = int(n)

base_data1 = ["A", "T", "G", "C"]
base_data2 = ["A", "T", "G", "C"]


def kmer(base_data1, base_data2, n):
    if n < 2:
        return base_data2
    else:
        l_temp = []
        for base1 in base_data1:
            for base2 in base_data2:
                l_temp.append(base1 + base2)
        return kmer(base_data1, l_temp, n - 1)


kmer_list = kmer(base_data1, base_data2, n)

print(f"{n}mer: ", kmer_list)
