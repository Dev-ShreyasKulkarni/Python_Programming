def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened")
        
        print(f"File offset is {fobj.tell()}") #0
        data = fobj.read(10)
        print(data)
        print(f"File offset is {fobj.tell()}") #10

        data = fobj.read(10)
        print(data)
        print(f"File offset is {fobj.tell()}") #20
        
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File does not exist",fobj)
    
if __name__ == "__main__":
    main()