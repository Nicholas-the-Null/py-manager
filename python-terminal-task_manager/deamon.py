import psutil
import os
from main.asset.secure.file_sha256 import File_calcolatore_sha256







def monitor_process(process,status,action):
    name_process=process
    process_status=status
    if status in ["off","on"]==False:
        print("error")
    else:
        final_action=action
        if final_action in ["close","alert"]:
            while True:
                if process in (p.name() for p in psutil.process_iter()) and process_status=="off":#se il processo è attivo ed il pragma è on vuol dire che non si è chiuso
                    if final_action=="close":
                        #terminate process
                        for proc in psutil.process_iter():
                            if proc.name() == process:
                                proc.kill()


                        
                    elif final_action=="alert":
                        print("deamon : process "+process+" is running")
                        print('\007')
                        exit()
        else:
            print("error")
    exit()

def monitor_file(file,status,action):
    name_file=file
    file_status=status
    if status in ["edit","other"]==False or os.path.exists(name_file) is False:
        print("erroreee")
        exit()
    else:
        sha256=File_calcolatore_sha256(name_file)
        final_action=action
        if final_action=="alert":
            while True:
                if os.path.exists(name_file)==False and file_status=="other":
                    print("file "+name_file+" is deleted or changed path") 
                    print('\007')
                    exit()
                elif os.path.exists(name_file) and file_status=="edit":
                    sha256_new=File_calcolatore_sha256(name_file)
                    if sha256_new!=sha256:
                        print("deamon: file "+name_file+" is changed")
                        print('\007')
                        exit()
                    
                else:
                    exit()
        else:
            print("erroro")
    exit()

def monitor_path(path,status,action):
    name_path=path
    path_status=status
    if status in ["delete","change"]==False or os.path.exists(name_path)==False or os.path.isdir(name_path)==False:
        print("error")
        exit()
    else:
        size = 0
        for path, dirs, files in os.walk(name_path):
            for f in files:
                fp = os.path.join(path, f)
                size += os.path.getsize(fp)
        
        final_action=action
        if final_action =="alert":
            while True:
                if os.path.exists(name_path)==False and path_status=="delete":
                    print("deamon:path "+name_path+" is deleted") 
                    exit()
                elif os.path.exists(name_path) and path_status=="change":
                    size_new = 0
                    for path, dirs, files in os.walk(name_path):
                        for f in files:
                            fp = os.path.join(path, f)
                            size_new += os.path.getsize(fp)
                    if size_new!=size:
                        print("path "+name_path+" is changed")
                        print('\007')
                        exit()
                    
                else:
                    break
        else:
            print("error")
    exit()

    