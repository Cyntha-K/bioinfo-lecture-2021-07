file_name = "write_sample2.txt"

handle = open(file_name, "w")
handle.write("Hello\n")
handle.write("bioinformatics\n")

with open(file_name, "a") as handle:
    handle.write("ken\n")

s = "s1, s2, s3" #csv
data = s.split("\t")
print(data) #['s1', 's2', s3']

with open(file_name, "a") as handle:
    handle.write("\t".join(data) + "\n")

