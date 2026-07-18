def SumEven(No):
    sum=0
    for i in range(2,No,2):
        sum+=i
    
    print(f"Sum Even is {sum}")
    
def SumOdd(No):
    sum=0
    for i in range(1,No,2):
        sum+=i
            
    print(f"Sum Odd is {sum}")

def main():
    SumEven(10000000)
    SumOdd(10000000)
    
if __name__ == "__main__":
    main()