import time
import client_logon
from threading import Thread

def connect():
    client_logon.logon("client_FIXT11.cfg")

def check():

    if client_logon.isConnected == True:
        print ("True")

    else:
        print("False")

if __name__ == "__main__":
    Thread(target = connect).start()
    while 1:
        time.sleep(5)
        Thread(target = check).start()
