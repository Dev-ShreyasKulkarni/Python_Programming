def SumCube(no):
    sum=0
    for i in range(1,no+1):
        sum+=i*i*i
    
    return sum
    
def main():
    no = 5
    ret = SumCube(no)
    print(f"Sum of cubes till {no} : {ret}")

if __name__ == "__main__":
    main()