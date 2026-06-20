from Marvellous import Addition

def main():
    print("Enter the first number: ")
    value1 = int(input())
    print("Enter the first number: ")
    value2 = int(input())

    ret = Addition(value1,value2)
    print("Addition is :",ret)
    
    ret = Substraction(value1,value2) #error
    print("Substraction is :",ret)
    
    
if __name__ == "__main__":
    main()