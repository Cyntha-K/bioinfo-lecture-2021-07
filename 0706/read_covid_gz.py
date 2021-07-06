import gzip 

file_name = "covid19.fasta.gz"

data = dict()

with gzip.open(file_name, 'rt') as handle:
#with gzip.open(file_name, 'rb') as handle:
    for line in handle:
        #line = line.decode("utf-8")
        if line.startswith(">"):
            continue
        for base in line.strip():
            if base not in data:
                data[base] = 0
            data[base] += 1

print(data)



