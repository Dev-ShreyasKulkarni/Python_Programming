import sys,os,time

def Directory_Scanner(directory_path):
    timestamp = time.ctime()
    log_filename = "Marvellous%s.log"%(timestamp)
    log_filename = log_filename.replace(" ","_")
    log_filename = log_filename.replace(":","_")
    print("Log File gets created with the name : ",log_filename)
    fobj = open(log_filename,"w")
    fobj.write("Marvellous Automation Script \n")
    fobj.write("Files from the directory are : \n")
    
    for folderName,subFolder,fileName in os.walk(directory_path):
        for fname in fileName:
            fobj.write(fname+"\n")
    
    fobj.close()

def main():
    Border = '-'*55
    print(Border)
    print("Marvellous Automation Script")
    print(Border)
    
    
    if len(sys.argv) == 2:
        
        if sys.argv[1] in ['--h','--H']:
            print("This automation script is used to travel the directory")
            print("For better usage, please use --u flag")
        elif sys.argv[1] in ['--u','--U']:
            print("Please execute the script as ")
            print("python filename.py DirectoryName")
            print("Directory name should be absolute path")
        else: 
            Directory_Scanner(sys.argv[1])
            
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
        
        
    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border)
        
if __name__ == "__main__":
    main()