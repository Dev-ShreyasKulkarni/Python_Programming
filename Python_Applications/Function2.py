def Addition(no1,no2):
    ans = no1 + no2
    return ans
    
def main():
    print("Enter the first number: ")
    value1 = int(input())
    print("Enter the first number: ")
    value2 = int(input())

    ret = Addition(value1,value2)
    print("Addition is :",ret)
    
    
    
if __name__ == "__main__":
    main()