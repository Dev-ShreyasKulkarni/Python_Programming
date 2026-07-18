import os

def main():
    ret = os.path.exists("Demo.txt")
    
    if ret:
        print("File is present in current directory")
    else:
        print("No such File is present in current directory")
        
if __name__ == "__main__":
    main()