  
Seq1 = "ATGTTATAG"

for i in range(0,len(Seq1),3):
    #print(i) # 0 3 6 
    #print(i, Seq1[i]) # 인덱싱
    print(i, i+3, Seq1[i:i+3]) # 슬라이싱
