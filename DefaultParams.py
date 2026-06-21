def Area(radius,PI=3.14):
    ans = PI*radius*radius
    return ans
    
def main():
    ret = Area(10.5)
    print("Area is :",ret)
    
    ret = Area(10.5,7.12)
    print("Area is :",ret)

if __name__ == "__main__":
    main()