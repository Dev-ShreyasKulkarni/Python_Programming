import os

def main():
    for folderName,subFolder,FileName in os.walk("Marvellous"):
        print("Folder name :",folderName)
        for subF in subFolder:
            print("Sub Folder name :",subF)
        
            
if __name__ == "__main__":
    main()