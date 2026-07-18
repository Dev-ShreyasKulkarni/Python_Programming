import os

def main():
    try:
        # fobj.remove() -> Not Applicable
        os.remove("Demo.txt")
        #  Deletes Permanently
        
    except FileNotFoundError as fobj:
        print("File does not exist",fobj)
    
if __name__ == "__main__":
    main()