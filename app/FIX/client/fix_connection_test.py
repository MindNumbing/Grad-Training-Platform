import time
import fix_client
from threading import Thread

def isConnected():
    if fix_client.isConnected is True:
        print("Quickfix Client is connected")
        return True
    elif fix_client.isConnected is False:
        print("Quickfix client is not connected")
        return False
    elif fix_client.isConnected is None:
        print("Quickfix Client has not been initialized")
        return False

def isConnectedText():
    if isConnected() is True:
        return 'Connected'
    elif isConnected() is False:
        return 'Disconnected'

def  connect_client(client_version):
    if not isConnected():
        if client_version == 'FIXT-1.1':
            Thread(target=fix_client.connect).start()


def disconnect():
    if isConnected():
        fix_client.disconnect()

if __name__ == "__main__":
    connect_client('FIXT-1.1')
    while 1:
        time.sleep(1)
        isConnected()

