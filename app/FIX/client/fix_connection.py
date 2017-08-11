import time
import fix_client as fix_client
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

