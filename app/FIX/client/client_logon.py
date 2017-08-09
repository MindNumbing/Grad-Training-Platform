import time
import quickfix
from   qfix_app_BME import Application

isConnected = None

def logon(thisFile):

    try:
        settings = quickfix.SessionSettings(thisFile)
        application = Application()
        storeFactory = quickfix.FileStoreFactory(settings)
        #logFactory = fix.ScreenLogFactory(settings)
        logFactory = quickfix.FileLogFactory(settings)
        initiator = quickfix.SocketInitiator(application,
                                           storeFactory,
                                           settings,
                                           logFactory)
        initiator.start()
        while 1:
            time.sleep(1)
            global isConnected
            isConnected = initiator.isLoggedOn()
    except (fix.ConfigError, fix.RuntimeError) as e:
        print(e)

