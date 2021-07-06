seq = input('seq?')

seq = seq.lower()

seq = seq.replace('a', 'T')
seq = seq.replace('c', 'G')
seq = seq.replace('t', 'A')
seq = seq.replace('g', 'C')

print(seq)

