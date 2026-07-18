def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened")
        
        print(f"File offset is {fobj.tell()}")
        data = fobj.read(10)
        print(f"File offset is {fobj.tell()}")

        print(data)
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File does not exist",fobj)
    
if __name__ == "__main__":
    main()