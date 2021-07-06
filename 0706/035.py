d_count = {}

list = [3, 1, 1, 2, 0, 0, 2, 3, 3,]

for r in list:
    d_count[r] = d_count.get(r, 0) +1

print(d_count)

