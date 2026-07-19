import sys

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] in ['--h','--H']:
            print("Help")
        elif sys.argv[1] in ['--u','--U']:
            print("Usage")
        else: 
            directory_name = sys.argv[1]
            print(f"Directory name is : {directory_name}")
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
if __name__ == "__main__":
    main()