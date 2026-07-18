

def main():
    ans = 0
    try:
        no1= int(input("Enter first no : "))
        no2= int(input("Enter second no : "))
        
        ans= no1/no2
        
        print("Division is successful")
        
    except ZeroDivisionError as zobj:
        print("Exception occured due to second operand is zero",zobj)
        
    except ValueError as vobj:
        print("Exception occurred due to invalid datatype",vobj)
        
    print(f"Result is : {ans}")
    
if __name__ == "__main__":
    main()