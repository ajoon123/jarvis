import time
import datetime
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:  
        return False

if is_admin:
    current_time = datetime.datetime.now().strftime("%H:%M")
    stop_time = input("Enter time eg:- [10:10] :-")
    a = current_time.replace(":",".")
    a = float(a)
    b = stop_time.replace(":",".")
    b = float(b)
    Focus_Time = b-a
    Focus_time = round(Focus_Time,3)

    host_path = "C:\Windows\System32\drivers\etc\hosts"
    redirect = "127.0.0.1"


    print(current_time)
    time.sleep(2)
    website_list =["www.facebook.com","facebook.com","www.instagram.com","instagram.com","www.youtube.com","youtube.com"]
    if (current_time<stop_time):
        with open(host_path,"r+") as file:
            content = file.read()
            time.sleep(2)
            for website in website_list:
                if website in content:
                     pass
            else:    
                file.write(f"{redirect} {website}")
                print("Done")
                time.sleep(1)

            print(" FOCUS MODE TURNED ON !!")    

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        website_list =["www.facebook.com","facebook.com","www.instagram.com","instagram.com","www.youtube.com","youtube.com"]
        if (current_time >=stop_time):
            with open(host_path,"r+") as file:
                content = file.readlines()
                file.seek(0)

                for line in content:
                    if  not any(website in line for website in website_list):
                        file.write(line)

                file.truncate()        

                print("WEBSITE ARE UNBLOCKED")
                file = open("focus.txt","a")
                file.write(f",{Focus_Time}")
                file.close()
                break

else:
    ctypes.windll.shell32.shellExecuteW(None,"runas",sys.excutables," ".join(sys.argv),None,-1)
