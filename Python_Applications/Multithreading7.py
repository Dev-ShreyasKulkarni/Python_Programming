import time,threading

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
    t1=threading.Thread(target=SumEven,args=(100000000,))
    t2=threading.Thread(target=SumOdd,args=(100000000,))

    start = time.perf_counter()
    t1.start()
    t2.start()
    end = time.perf_counter()
    
    print(f"Time taken is is {end-start:.4f}")
    
if __name__ == "__main__":
    main()