import sys,os,time,schedule

def Directory_Scanner(directory_path = "Marvellous"):
    Border = '-'*55
    timestamp = time.ctime()
    log_filename = "Marvellous%s.log"%(timestamp)
    log_filename = log_filename.replace(" ","_")
    log_filename = log_filename.replace(":","_")
    
    Ret = False
    
    # Check if it exists
    Ret = os.path.exists(directory_path)
    if Ret == False: 
        print(f"Marvellous Automation Error : There is no such directory with name {directory_path}")
        return 
    
    # Check if it is a directory
    Ret = os.path.isdir(directory_path)
    if Ret == False: 
        print(f"Marvellous Automation Error : It is not a directory with name {directory_path}")
        return 
    
    
    print("Log File gets created with the name : ",log_filename)
    fobj = open(log_filename,"w")
    
    fobj.write(Border+"\n")
    fobj.write("Marvellous Automation Script \n")
    fobj.write(Border+"\n\n")
    
    fobj.write("Files from the directory are : \n\n")
    fobj.write(Border+"\n\n")

    for folderName,subFolder,fileName in os.walk(directory_path):
        for fname in fileName:
            fname = os.path.join(folderName,fname)
            fobj.write(fname+"\n")
            print(f"File name : {fname}, size : {os.path.getsize(fname)} bytes")
    
    fobj.write(Border+"\n")
    fobj.write("Log file gets created at : %s"%timestamp)
    fobj.write("\n"+Border+"\n")
    
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
            # schedule.every(1).minute.do(Directory_Scanner,sys.argv[1])
            Directory_Scanner(sys.argv[1])
            while True:
                schedule.run_pending()
                time.sleep(1)
            
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
        
        
    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border)
        
if __name__ == "__main__":
    main()