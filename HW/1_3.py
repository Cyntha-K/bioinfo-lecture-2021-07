base_count = {"A":"Adenine", "C":"Cytosine", "G":"Guanine", "T":"Thymine", "U":"Uracil"}

seq = input('sequence?')

seq_data = ""

for i in seq:
    seq_data += ' ' + base_count[i]

print(seq_data)


