import pdb

def sum(maxint):
    s = 0
    for i in range(maxint):
        s += i
    return s

pdb.runcall(sum,10)
