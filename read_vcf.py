import sys

cnt = 0
with open(sys.argv[1],'r') as handle:
    for line in handle:
        if line.startswith('#'):
            continue
        cnt +=1

print(cnt)
