
num = int(input('input digit:'))

list00 = ['A','G','T','C']
nu = ''
for i in range(num):
    for j in list00:
        nu+=j
        if len(nu)==3:
            print(nu)
            nu==''
