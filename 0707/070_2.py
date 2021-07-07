cnt_all = 0
cnt_pass = 0

with open("070.vcf", "r") as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        data = line.strip().split("\t")
        cnt_all += 1
        if data[6] == "PASS":
            cnt_pass += 1

print(cnt_pass, cnt_all, cnt_pass / cnt_all)
