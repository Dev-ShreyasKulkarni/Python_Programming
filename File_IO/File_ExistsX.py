import os

def main():
    if os.path.exists("Demo.txt"):
        print("File is present in current directory")
    else:
        print("No such File is present in current directory")
        
if __name__ == "__main__":
    main()