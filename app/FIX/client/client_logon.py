import time
import quickfix
from qfix_app_BME import Application

isConnected = None


def logon(this_file):

    try:
        settings = quickfix.SessionSettings(this_file)
        application = Application()
        store_factory = quickfix.FileStoreFactory(settings)
        #logFactory = fix.ScreenLogFactory(settings)
        log_factory = quickfix.FileLogFactory(settings)
        initiator = quickfix.SocketInitiator(application,
                                             store_factory,
                                             settings,
                                             log_factory)
        initiator.start()
        while 1:
            time.sleep(1)
            global isConnected
            isConnected = initiator.isLoggedOn()
    except (quickfix.ConfigError, quickfix.RuntimeError) as e:
        print(e)



def logout(this_file):
