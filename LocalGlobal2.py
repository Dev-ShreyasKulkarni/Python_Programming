no = 11 #Global Variable

def Display():
    a = 21 #Local Variable
    print("From display : ",no)
    print("From display value of a is : ",a)

def Demo():
    print("From display value of a is : ",a)
    print("From demo : ",no)


Display()
Demo()