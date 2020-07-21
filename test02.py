import sys

f = sys.argv[1]
res =''
with open(f,'w') as handle:
    if handle.startswith('>'):
        continue
    else:
        res += handle.read()
        res += handle.read()
print(res)
