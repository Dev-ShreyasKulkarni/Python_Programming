import sys,os,hashlib

def CalculateCheckSum(filename):
    fobj = open(filename,"rb")
    hobj = hashlib.md5()
    
    Buffer = fobj.read(1024)
    
    while len(Buffer)>0:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()

def FindDuplicate(directory_name):
    Ret = False
    Ret = os.path.exists(directory_name)
    
    if Ret == False:
        print("Path is Invalid")
        return
    
    Ret = os.path.isdir(directory_name)
    
    if Ret == False:
        print("Not a Directory")
        return
    
    for folderName, subFolder, filename in os.walk(directory_name):
        for fname in filename:
            fname = os.path.join(folderName,fname)
            checksum = CalculateCheckSum(fname)
            print(f"{fname}:{checksum}")
    
    
def main():
    FindDuplicate("Test")
    
if __name__ == "__main__":
    main()