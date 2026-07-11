class Arithmetic:
    def Addition(self,no1,no2):
        return no1+no2 

    def Substraction(self,no1,no2):
        return no1-no2 
    
    
Aobj= Arithmetic()

no1= int(input("Enter a no : "))
no2= int(input("Enter a no : "))


print(f"Addition is {Aobj.Addition(no1,no2)}")
# Internally interprets as below
# print(f"Addition is {Addition(Aobj,no1,no2)}") 
print(f"Substraction is {Aobj.Substraction(no1,no2)}")