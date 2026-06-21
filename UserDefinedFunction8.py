def BigBazar():
    print("Inside Big Bazar")
    
    def Amul():
        print("Inside Amul Icecream Parlour")
        
        
def main():
    BigBazar()
    Amul() #error
    BigBazar.Amul() #error
    
if __name__ == '__main__':
    main()