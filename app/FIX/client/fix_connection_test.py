import time
import fix_client
from threading import Thread

def isConnected():
    '''This is a check to see whether or not the fix client is connected to the BME simulator
    
    Returns:
        returns a boolean of the connection status (True=Connected, False=Not-Connected) if the client has been initialized or else returns none
    '''
    if fix_client.isConnected is True:
        print("Quickfix Client is connected")
        return True
    elif fix_client.isConnected is False:
        print("Quickfix client is not connected")
        return False
    elif fix_client.isConnected is None:
        print("Quickfix Client has not been initialized")
        return False

<<<<<<< HEAD
def connect_client(client_version):
=======
def isConnectedText():
    '''This is a text representation of the connection status

    Returns:
        connected if the isConnected() returns True
        disconnected if the isConnected() returns False
    '''
    if isConnected() is True:
        return 'Connected'
    elif isConnected() is False:
        return 'Disconnected'

def  connect_client(client_version):
>>>>>>> c37c62f9d4dac969f0543dbab8016541ff30e7d6
    '''This initiates the logon for the fix client to the BME simulator if it is not already connected
    
    Args:
        client_version:String- This is the fix version that they want to connect to
    '''
    if not isConnected():
        if client_version == 'FIXT-1.1':
<<<<<<< HEAD
            Thread(target=fix_client.connect).start()
=======
            Thread(target=fix_client.connect, args=('client_FIXT11.cfg',)).start()
>>>>>>> c37c62f9d4dac969f0543dbab8016541ff30e7d6

def disconnect():
    '''This disconnects the fix client from the BME if it is already connected'''
    if isConnected():
<<<<<<< HEAD
        fix_client.disconnect()
=======
        fix_client.disconnect()

if __name__ == "__main__":
    connect_client('FIXT-1.1')
    while 1:
        time.sleep(1)
        isConnected()
        
>>>>>>> c37c62f9d4dac969f0543dbab8016541ff30e7d6
