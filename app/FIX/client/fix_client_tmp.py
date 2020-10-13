import time
import quickfix
from qfix_app_BME_tmp import Application

isConnected = None
keep_open = None

def connect(config_file):
    keep_open = True
    
    try:
        settings = quickfix.SessionSettings(config_file)
        application = Application()
        store_factory = quickfix.FileStoreFactory(settings)
        log_factory = quickfix.FileLogFactory(settings)
        initiator = quickfix.SocketInitiator(application,
                                             store_factory,
                                             settings,
                                             log_factory)

        initiator.start()

        while keep_open:
            time.sleep(1)
            global isConnected
            isConnected = initiator.isLoggedOn()


        initiator.stop()
    except (quickfix.ConfigError, quickfix.RuntimeError) as e:
        print(e)

def disconnect():
    global keep_open
    keep_open = False
