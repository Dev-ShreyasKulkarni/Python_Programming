# seek(upto,from_where)
# from_where - 0/1/2
# 0 - Start
# 1 - Current
# 2 - End


def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened")
        
        fobj.seek(10,0)
        
        Data = fobj.read()
        
        print(Data)
        
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File does not exist",fobj)
    
if __name__ == "__main__":
    main()