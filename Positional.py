def Area(radius,PI):
    ans = PI*radius*radius
    return ans
    
def main():
    ret = Area(10.5,3.14)
    print("Area is :",ret)
    
    ret = Area(13.6,7.12)
    print("Area is :",ret)
    
if __name__ == "__main__":
    main()