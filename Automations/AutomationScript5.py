import sys

def main():
    print('-'*50)
    print("Marvellous Automation Script")
    print('-'*50)
    
    
    if len(sys.argv) == 2:
        if sys.argv[1] in ['--h','--H']:
            print("This automation script is used to travel the directory")
            print("For better usage, please use --u flag")
        elif sys.argv[1] in ['--u','--U']:
            print("Please execute the script as ")
            print("python filename.py DirectoryName")
            print("Directory name should be absolute path")
        else: 
            directory_name = sys.argv[1]
            print(f"Directory name is : {directory_name}")
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
        
        
    print('-'*50)
    print("Thank you for using Marvellous Automation Script")
    print('-'*50)
        
if __name__ == "__main__":
    main()