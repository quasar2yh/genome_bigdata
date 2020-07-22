def mer(l1,l2,n):
    if n==1:
        return l2
    else:
        ltmp=[]
        for i in l1:
            for j in l2:
                ltmp.append(i+j)  
        return mer(l1,ltmp,n-1)
    

list1 = ['A','T','G','C']
list2 = ['A','T','G','C']
n = int(input('input k-mer:'))
print(mer(list1,list2,n))
