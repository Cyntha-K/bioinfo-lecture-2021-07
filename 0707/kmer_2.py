import sys

def rec(l1, l2, n):
    if n <2:
        return l2
    else:
        ltmp = []
        for s1 in l1:
            for s2 in l2:
                ltmp.append(s1+s2)
        return rec(l1, ltmp, n-1)


l1 = ["A", "T", "G", "C"]
l2 = ["A", "T", "G", "C"]
n = int(sys.argv[1])
l = rec(l1, l2, n)
print(l)
