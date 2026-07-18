import time,multiprocessing,os

def SumCube(no):
    print("Process is running with pid : ",os.getpid())
    sum=0
    for i in range(1,no+1):
        sum+=i**3
    
    return sum
    
def main():
    data = [10000000,20000000,30000000,40000000,50000000]
    result = list()
    
    start = time.perf_counter()

    pobj=multiprocessing.Pool()
    result = pobj.map(SumCube,data)
    pobj.close()
    pobj.join()
    
    end = time.perf_counter()
    
    print(f"Result is {result}")
    print(f"Time taken is {end-start:.4f} seconds")

if __name__ == "__main__":
    main()