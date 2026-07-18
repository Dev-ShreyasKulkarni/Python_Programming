class Demo:
    # Class Variables
    Value1 = 10
    Value2 = 20
    
    # Constructor
    def __init__(self):
        # Instance Variables
        self.No1 = 11
        self.No2 = 21
    
    # Instance Method
    def fun(self):
        print("Inside Instance Method : fun")
        print(self.No1)
        print(self.No2)
        
        print(Demo.Value1)
        print(Demo.Value2)
        
    @classmethod
    def gun(cls):
        print("Inside Class Method : gun")
        
        # Instance variables cannot be accessed by class name because 
        # instance is not created to allocate memory
        
        # print(Demo.No1)
        # print(Demo.No2)
        
        print(cls.Value1)
        print(cls.Value2)
        
    @staticmethod
    def sun():
        print("Inside Static Method : sun")
        print(Demo.Value1)
        print(Demo.Value2)
        
        
# Instance Creation
dobj = Demo()
dobj.fun()

# Call without object
Demo.gun()
# Call with object
dobj.gun()


Demo.sun()
