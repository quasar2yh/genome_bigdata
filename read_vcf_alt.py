import sys

l = []
with open(sys.argv[1],'r') as handle:
    for line in handle:
        if line.startswith('#'):
            continue
        splitted = line.strip().split('\t')
        if ',' in splitted[4]:
            sub = splitted[4].split(',')
            l.extend(sub)
        else:
            l.append(splitted[4])
print(len(l))

insertion =0
deletion =0
snp=0

with open(sys.argv[1],'r') as handle:
    for line in handle:
        if line.startswith('#'):
            continue
        splitted = line.strip().split('\t')
        ref = splitted[3]
        alt = splitted[4]
        if ','in alt or len(ref)==len(alt):
            snp+=1
        elif len(ref)>len(alt):
            deletion+=1
            print('deletion: ',ref,alt)
        elif len(ref)<len(alt):
            insertion+=1
            print('insertion: ',ref,alt) 
# if there are unexpected condition, error will arise
        else:
            raise           
print(f'{insertion} is/are insertion')
print(f'{deletion} is/are deletion')
