def main():
    try:
        open("Demo.txt","w")
        print("File gets opened")
    except FileNotFoundError as fobj:
        print("File does not exist",fobj)
    
if __name__ == "__main__":
    main()