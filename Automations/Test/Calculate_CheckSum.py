import sys,os,hashlib

def CalculateCheckSum(filename):
    fobj = open(filename,"rb")
    hobj = hashlib.md5()
    
    Buffer = fobj.read(1000)
    
    while len(Buffer)>0:
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()
    return hobj.hexdigest()
def main():
    ret = CalculateCheckSum("Demo.txt")
    print("Checksum of File is ",ret)
    
if __name__ == "__main__":
    main()