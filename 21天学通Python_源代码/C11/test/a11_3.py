import os

filenames = []

for a,b,files in os.walk('test'):
    if files:
        filenames.append([file[:-4] for file in files])

fname = 'testexam'
i = 0
for files in filenames:
    f=open(fname+str(i)+'.xls','w')
    for name in files:
        f.write(name[-2:]+'\t'+name[:-2]+'\n')
    f.close()
    i += 1
