print("-------------- Ticket Counter ---------------")
print("Please enter your age : ")
age = int(input())

if age <= 5:
    print("Free entry")
elif age > 5 and age <= 18:
    print("900")
elif age > 18 and age <= 40:
    print("1200")
else :
    print("500")
