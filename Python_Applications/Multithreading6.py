import time

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
    start = time.perf_counter()
    SumEven(100000000)
    SumOdd(100000000)
    end = time.perf_counter()
    
    print(f"Time taken is is {end-start:.4f}")
    
if __name__ == "__main__":
    main()