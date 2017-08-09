import sys
import time
import quickfix as fix
from   qfix_app import Application


try:
    thisFile = sys.argv[1]
    settings = fix.SessionSettings(thisFile)
    application = Application()
    storeFactory = fix.FileStoreFactory(settings)
    logFactory = fix.ScreenLogFactory(settings)
    initiator = fix.SocketInitiator(application,
                                       storeFactory, 
                                       settings,
                                       logFactory)
    initiator.start()
    while 1:
        time.sleep(1)
except (fix.ConfigError, fix.RuntimeError) as e:
    print(e)
