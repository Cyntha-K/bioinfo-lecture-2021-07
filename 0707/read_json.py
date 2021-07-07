import json

with open("data.json", "r") as handle:
    data = json.load(handle)


for elem in data:
    print(f"{elem['id']}\t{elem['sequence']}\t{elem['species']}")


# print(data)
# print(data.csv)
