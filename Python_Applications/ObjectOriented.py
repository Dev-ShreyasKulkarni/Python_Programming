class Arithmetic:
    def Addition(no1,no2):
        return no1+no2 

    def Substraction(no1,no2):
        return no1-no2 
    
    
Aobj= Arithmetic()

no1= int(input("Enter a no : "))
no2= int(input("Enter a no : "))

print(f"Addition is {Aobj.Addition(no1,no2)}") # ERROR
print(f"Substraction is {Aobj.Substraction(no1,no2)}")