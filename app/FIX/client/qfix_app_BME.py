import threading
import quickfix as fix


class Application (fix.Application):

    def onCreate(self, sessionID):
        self.sessionID = sessionID
        self.logon_event = threading.Event()
        print("Application created - session: " + sessionID.toString())


    def onLogon(self, sessionID):
        print "Logon", sessionID
        print 'setting event...'
        self.logon_event.set()


    def onLogout(self, sessionID):
        print "Logout", sessionID


    def toAdmin(self, message, sessionID):
        if message.getHeader().getField(35)=="A":
            header = message.getHeader()
            message.setField(fix.DefaultApplVerID(fix.ApplVerID_FIX42))
            message.setField(fix.EncryptMethod(fix.EncryptMethod_NONE))
            message.setField(fix.DefaultCstmApplVerID("T4.0"))
            header.setField(fix.SenderSubID("SID"))
            header.setField(fix.TargetSubID("TID"))

        pass


    def fromAdmin(self, message, sessionID):
       
        pass

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)
        # On log in accepted

        print "IN", message

    
    def toApp(self, message, sessionID):
        print "OUT", message

        
    def send(self, message):
        fix.Session.sendToTarget(message, self.sessionID)

    def onMessage(self, message, sessionID):
        print "OnMessage %s" % message

