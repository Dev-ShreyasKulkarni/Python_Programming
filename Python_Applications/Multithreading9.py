import time,threading

def SumEven(No):
    print("TID of SumEven Thread is :",threading.get_ident())
    
def SumOdd(No):
    print("TID of SumOdd Thread is :",threading.get_ident())


def main():
    print("TID of Main Thread is :",threading.get_ident())

    t1=threading.Thread(target=SumEven,args=(100000000,))
    t2=threading.Thread(target=SumOdd,args=(100000000,))

    start = time.perf_counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.perf_counter()
    
    print(f"Time taken is is {end-start:.4f}")
    
if __name__ == "__main__":
    main()