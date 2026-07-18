CheckEven = lambda no: no%2 == 0
Increment = lambda no:no+1
Addition = lambda no1,no2:no1+no2

def filterX(task,Elements):
    Result = list()
    
    for no in Elements:
        Ret = task(no)
        if Ret:
            Result.append(no)
    
    return Result

def mapX(task,Elements):
    Result = list()
    
    for no in Elements:
        Ret = task(no)
        Result.append(Ret)
    
    return Result

def reduceX(task,Elements):
    Sum = 0
    for no in Elements:
        Sum = task(Sum,no)
    return Sum

def main():
    Data = [13,12,8,10,11,20]
    print("Input Data is : ",Data)
    
    FData = list(filterX(CheckEven,Data))
    print("Data after filter : ",FData)
    
    MData = list(map(Increment,FData))
    print("Data after Map : ",MData)
    
    RData = reduceX(Addition,MData)
    print("Data after Reduce : ",RData)

    
if __name__ == "__main__":
    main()