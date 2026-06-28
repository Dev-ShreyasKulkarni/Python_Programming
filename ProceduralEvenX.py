def CheckEven(no):
    if no%2 == 0:
        return True
    else:
        return False
      
def main():
    value = int(input("Enter a no : "))
    ret = CheckEven(value)
    if ret:
        print(f"{value} is even")
    else:
        print(f"{value} is odd")
    
    
if __name__ == "__main__":
    main()