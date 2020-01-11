
import os,time,threading
adbway="C:adb/adb.exe "
port=100
i=51

def run():
    time.sleep(5)
    os.system("taskkill -f -im adb.exe")



if __name__ == '__main__':
    thread1=threading.Thread(target=run)
    #thread1.setDaemon(True)
    while i<port:
        connect=adbway+"connect 10.10.45."+str(i)
        os.system(connect)
        print(1)
        reboot = adbway + "shell reboot"
        thread1.run()
        print(2)
        os.system(reboot)
        print(3)
        disconnect=adbway+"disconnect 10.10.45."+str(i)
        os.system(disconnect)
        print(4)
        print(i)
        #time.sleep(2)
        i+=1