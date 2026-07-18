def main():
    try:
        fobj = open("Demo.txt","w")
        print("File gets opened")
        fobj.write("Marvellous Infosystems")
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File does not exist",fobj)
    
if __name__ == "__main__":
    main()