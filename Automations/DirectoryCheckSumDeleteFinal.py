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
    
    duplicate = {}
    
    for folderName, subFolder, filename in os.walk(directory_name):
        for fname in filename:
            fname = os.path.join(folderName,fname)
            checksum = CalculateCheckSum(fname)
            
            if checksum in duplicate:
                duplicate[checksum].append(fname)
            else : 
                duplicate[checksum]=[fname]

    return duplicate
    
def DeleteDuplicates(directory_name):
    MyDict = FindDuplicate(directory_name)
    Result = list(filter(lambda x : len(x) > 1 ,MyDict.values()))

    count = 0
    totalDeleted = 0
    
    for value in Result:
        for subvalue in value:
            count += 1
            if count>1:
                os.remove(subvalue)
                print("Duplicate Found : ",subvalue)
                totalDeleted += 1
        count = 0
    
    print("Total Deleted files :",totalDeleted)

def main():
    DeleteDuplicates("Test")
    
    
if __name__ == "__main__":
    main()