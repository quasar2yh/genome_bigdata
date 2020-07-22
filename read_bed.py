import sys 

tot = 0
with open(sys.argv[1],'r') as handle:
    for line in handle:
        splitted = line.strip().split('\t')
        print(splitted)
        print(type(splitted))
        length = len(splitted[2])-len(splitted[1])
        tot += length
print(tot)
