import os

l=['M']
for i in range(1,23):
    l.append(str(i))
l.append('X')
l.append('Y')

for i in l:
    cmd = 'wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/chromosomes/chr{}.fa.gz'.format(i)
   # os.system(cmd) 
    os.system('gunzip chr{}.fa.gz'.format(i))
for i in l:
    cmd2 = 'cat chr{}.fa >> hg19.fa'.format(i)
    os.system(cmd2)

