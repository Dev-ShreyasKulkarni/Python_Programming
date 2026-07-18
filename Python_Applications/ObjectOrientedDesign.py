class Arithmetic:
    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B
        
    # Instance Method
    def Addition(self):
        return self.no1+self.no2

    def Substraction(self):
        return self.no1-self.no2
    
    


val1= int(input("Enter a no : "))
val2= int(input("Enter a no : "))

Aobj= Arithmetic(val1,val2)

print(f"Addition is {Aobj.Addition()}")
# Internally interprets as below
# print(f"Addition is {Addition(Aobj)}") 
print(f"Substraction is {Aobj.Substraction()}")