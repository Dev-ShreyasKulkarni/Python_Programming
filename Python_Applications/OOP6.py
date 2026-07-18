class Demo:
    # Class Variables
    Value1 = 10
    Value2 = 20
    
    # Constructor
    def __init__(self):
        # Instance Variables
        self.No1 = 11
        self.No2 = 21
    
    
# Instance Creation
dobj1 = Demo()
dobj2 = Demo()

dobj1.No1 = 0

print(dobj1.No1) #0
print(dobj2.No1) #11

print(Demo.Value1) #10
Demo.Value1 = 0
print(Demo.Value1) #0