def Calculation(no1,no2):
    Mult = no1*no2
    Div = no1/no2
    
    return Mult,Div

def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))
    
    ret1,ret2 = Calculation(value1,value2)
    
    print("Multiplication is :",ret1)
    print("Division is :",ret2)

    
if __name__ == '__main__':
    main()