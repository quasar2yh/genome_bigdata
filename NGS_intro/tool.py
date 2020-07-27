import sys

class FASTA:
    def __init__(self, file_name: str):
        self.file_name=file_name
        self.count={}
        self.length=0
    def count_base(self):
        with open(self.file_name,'r') as handle:
            for line in handle :
                if line.startswith('>'):
                    continue
                line = line.strip()
                for s in line:
                    if s in self.count:
                        self.count[s]+=1
                    else:
                        self.count[s]=1
                 
    def get_length(self):
        for k,v in self.count.items():
            self.length += v
            print(v)    

    def __len__(self):
        self.get_length()
        return self.length


if __name__ == "__main__":
    if len(sys.argv)!=2:
        print(f'#usage: {sys.argv[0]} [fasta]')
        sys.exit()
    f = sys.argv[1]
    t = FASTA(f)
    t.count_base()
    print(t.count)
    t.get_length()
    print(t.length)
    


