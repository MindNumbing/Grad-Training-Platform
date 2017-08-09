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
    except (fix.ConfigError, fix.RuntimeError) as e:
        print(e)
