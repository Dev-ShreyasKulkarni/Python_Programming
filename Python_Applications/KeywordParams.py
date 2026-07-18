def Area(radius,PI):
    ans = PI*radius*radius
    return ans
    
def main():
    ret = Area(PI=3.14,radius=10.5)
    print("Area is :",ret)

if __name__ == "__main__":
    main()