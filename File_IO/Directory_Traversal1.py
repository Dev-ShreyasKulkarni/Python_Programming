import os

def main():
    for folderName,subFolder,FileName in os.walk("Marvellous"):
        print(folderName)
            
if __name__ == "__main__":
    main()