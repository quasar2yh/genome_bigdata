import sys

cnt=0
with open(sys.argv[1],'r') as handle:
    for line in handle:
        if line.startswith('#'):
            continue
        splitted = line.strip().split('\t')
        if splitted[6]=='PASS':
            cnt+=1

print(cnt)

re_cnt=0
l = []
d ={}
with open(sys.argv[1],'r') as handle:
    for line in handle:
        if line.startswith('#'):
            continue
        splitted = line.strip().split('\t')
        if splitted[2].startswith('rs'):
            chrom = splitted[0]
            pos = splitted[1]
            id_ = splitted[2]
            ref = splitted[3]
            alt = splitted[4]
            print(f'{chrom}-{pos}-{id_}-{ref}-{alt}')
            



