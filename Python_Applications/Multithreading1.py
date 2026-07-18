import threading

def Display():
    print("Inside display : ",threading.get_ident())   
     
def main():
    print("Inside Main : ",threading.get_ident())
    Display()
    
if __name__ == "__main__":
    main()