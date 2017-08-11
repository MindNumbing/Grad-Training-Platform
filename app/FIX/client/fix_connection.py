import time
<<<<<<< HEAD
import fix_connection_test as fix_client
=======
import fix_client as fix_client
>>>>>>> c37c62f9d4dac969f0543dbab8016541ff30e7d6
from threading import Thread

ConnectionStatus = None

def logon_status():
    global ConnectionStatus
    ConnectionStatus = True

def logoff_status():
    global ConnectionStatus
    ConnectionStatus = False

def isConnected():
    if ConnectionStatus is True:
        print("Quickfix Client is connected")
        return True
    elif ConnectionStatus is False:
        print("Quickfix client is not connected")
        return False
    elif ConnectionStatus is None:
        print("Quickfix Client has not been initialized")
        return False

def isConnectedText():
    if isConnected() is True:
        return 'Connected'
    elif isConnected() is False:
        return 'Disconnected'

def connect_client(client_version):
    if not isConnected():
        if client_version == 'FIXT-1.1':
            Thread(target=fix_client.connect, args=('client_FIXT11.cfg',)).start()

def disconnect():
    if isConnected():
        fix_client.disconnect()

<<<<<<< HEAD
if __name__ == "__main__":
    connect_client('FIXT-1.1')
    while 1:
        time.sleep(1)
        isConnected()
=======
>>>>>>> c37c62f9d4dac969f0543dbab8016541ff30e7d6
