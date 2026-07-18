import os

def main():
    for folderName,subFolder,FileName in os.walk("Marvellous"):
        print("Folder name :",folderName)
        for subF in subFolder:
            print("Sub Folder name :",subF)
        for fname in FileName:
            print("File name :",fname)
            
if __name__ == "__main__":
    main()