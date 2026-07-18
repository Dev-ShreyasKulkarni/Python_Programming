def CheckEven(no):
    if no%2 == 0:
        print(f"{no} is even")
    else:
        print(f"{no} is odd")
      
def main():
    value = int(input("Enter a no : "))
    CheckEven(value)
    
    
if __name__ == "__main__":
    main()