import time,multiprocessing

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
    
    p1=multiprocessing.Process(target=SumEven,args=(100000000,))
    p2=multiprocessing.Process(target=SumOdd,args=(100000000,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    end = time.perf_counter()
    
    print(f"Time taken is is {end-start:.4f}")
    
if __name__ == "__main__":
    main()