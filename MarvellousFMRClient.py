from MarvellousLibrary import filterX,mapX,reduceX

CheckEven = lambda no: no%2 == 0
Increment = lambda no:no+1
Addition = lambda no1,no2:no1+no2

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