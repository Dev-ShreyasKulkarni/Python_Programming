import time

def factorial(no):
    facto = 1
    for i in range(1,no+1):
        facto = facto * i
    return facto


def main():
    no = int(input("Enter a number : "))
    start = time.perf_counter()
    ret = factorial(no)
    end = time.perf_counter()
    print(f"Factorial of {no} is {ret}")
    print(f"Time required is {end-start:.5f} seconds")
if __name__ == "__main__":
    main()