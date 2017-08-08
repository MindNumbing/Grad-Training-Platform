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
        message = fix.Message() 

        header = message.getHeader()
        trailer = message.getTrailer()

        header.setField(fix.BeginString(fix.BeginString_FIX42))
        header.setField(fix.BodyLength())
        header.setField(fix.MsgType(fix.MsgType_NewOrderSingle))
        header.setField(fix.SendingTime())
        header.setField(fix.SenderSubID("SG1"))
        header.setField(fix.TargetSubID("BARCA"))
        header.setField(fix.MsgSeqNum())
        
        message.setField(fix.ClOrdID("123"))
        message.setField(fix.HandlInst(fix.HandlInst_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION))
        message.setField(fix.Symbol("APPL"))
        message.setField(fix.Side(fix.Side_BUY))
        message.setField(fix.TransactTime())
        message.setField(fix.OrderQty(1000))
        message.setField(fix.OrdType(fix.OrdType_MARKET))
        message.setField(fix.Price(2000))

        trailer.setField (fix.CheckSum())
        application.send(message)

except (fix.ConfigError, fix.RuntimeError) as e:
    print(e)
