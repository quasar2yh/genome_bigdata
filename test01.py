s = 'AGTTTATAG'

for i in range(len(s)):
    if s[i:].find('TT'):
        print(i)


print('---------------------')

for i in range(0,len(s), 1):
    if s[i:i+2] == 'TT':
        print(i, i+1, s[i:i+2])


