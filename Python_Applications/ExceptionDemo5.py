

def main():
    ans = 0
    try:
        no1= int(input("Enter first no : "))
        no2= int(input("Enter second no : "))
        
        ans= no1/no2
        
        print("Division is successful")
    
    except Exception as eobj:
        print("Exception occured",eobj)
        
    
        
    print(f"Result is : {ans}")
    
if __name__ == "__main__":
    main()