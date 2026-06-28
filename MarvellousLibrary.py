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