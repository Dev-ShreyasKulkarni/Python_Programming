# Accept: Multiple parameters
# Return: Multiple values

def Marvellous(value1,value2):
    print("Inside Marvellous :",value1,value2)
    return 21,51

def main():
    ret1,ret2 = Marvellous(10,20)
    print("Return values are :",ret1,ret2)
    
if __name__ == '__main__':
    main()