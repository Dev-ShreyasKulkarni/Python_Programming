def main():
    try:
        open("Demo.txt","r")
        print("File gets opened")
    except FileNotFoundError as fobj:
        print("File does not exist",fobj)
    
if __name__ == "__main__":
    main()