
num = int(input('input digit:'))

nu =[]
nu_list=['A','T','G','C']

def kmer():
    for i in range(num):
        for j in nu_list:
            nu[i]=j
            if len(nu)==num:
                print(nu)

kmer()


    
    
