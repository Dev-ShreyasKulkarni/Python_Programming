CheckEven = lambda no:(no%2 == 0)
      
def main():
    value = int(input("Enter a no : "))
    ret = CheckEven(value) # ret = (no%2 == 0)
    if ret:
        print(f"{value} is even")
    else:
        print(f"{value} is odd")
    
    
if __name__ == "__main__":
    main()