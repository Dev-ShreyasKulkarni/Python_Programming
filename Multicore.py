import os

def main():
    print("No of cores are : ",os.cpu_count())  
      
if __name__ == "__main__":
    main()
    
    
facto = lambda x : x*facto(x-1) if x>0 else 1