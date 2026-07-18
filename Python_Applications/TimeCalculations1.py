def factorial(no):
    facto = 1
    for i in range(1,no+1):
        facto = facto * i
    return facto


def main():
    no = int(input("Enter a number : "))
    print(factorial(no))

if __name__ == "__main__":
    main()