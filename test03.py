import sys

def read_txt(file_name:str) -> str:
    ret =''
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            ret += line.strip()
    return ret

def read_csv(file_name:str)->str:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(',')
                continue
            imsi = line.strip().split(',')
            d = dict(zip(header, imsi))
            ret.append(d)
    return ret


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usage: python{sys.argv[0]} [txt]")
        sys.exit()

    file_name = sys.argv[1]
    txt = read_csv(file_name)
    print(txt)
