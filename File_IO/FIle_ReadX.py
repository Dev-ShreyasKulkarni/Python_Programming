def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened")
        data = fobj.read()
        print(data)
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File does not exist",fobj)
    
if __name__ == "__main__":
    main()