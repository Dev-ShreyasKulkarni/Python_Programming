import time

def factorial(no):
    facto = 1
    for i in range(1,no+1):
        facto = facto * i
    return facto


def main():
    no = int(input("Enter a number : "))
    start = time.time()
    ret = factorial(no)
    end = time.time()
    print(f"Factorial of {no} is {ret}")
    print(f"Time required is {end-start} seconds")
if __name__ == "__main__":
    main()