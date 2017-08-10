import threading
import quickfix as fix


class Application (fix.Application):

    def onCreate(self, sessionID):
        self.sessionID = sessionID
        self.logon_event = threading.Event()
        print("Application created - session: " + sessionID.toString())
        self.p('I am being created')

    def onLogon(self, sessionID):
        print "Logon", sessionID
        print 'setting event...'
        self.logon_event.set()
        self.p('I am logging on')

    def onLogout(self, sessionID):
        print "Logout", sessionID
        self.p('I am logging off')

    def toAdmin(self, message, sessionID):
        if message.getHeader().getField(35)=="A":
            header = message.getHeader()
            message.setField(fix.DefaultApplVerID(fix.ApplVerID_FIX42))
            message.setField(fix.EncryptMethod(fix.EncryptMethod_NONE))
            message.setField(fix.DefaultCstmApplVerID("T4.0"))
            header.setField(fix.SenderSubID("SID"))
            header.setField(fix.TargetSubID("TID"))
            self.p('I am sending to admin?')
        pass


    def fromAdmin(self, message, sessionID):
        self.p('Admin is sending to me')
        pass

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)
        # On log in accepted
        print "IN", message
        self.p('getting something from app')
    
    def toApp(self, message, sessionID):
        print "OUT", message
        self.p('Sending stuff to app')
        
    def send(self, message):
        fix.Session.sendToTarget(message, self.sessionID)
        self.p('sending something')

    def onMessage(self, message, sessionID):
        print "OnMessage %s" % message
        self.p('Getting something back')

    def p(self, text):
        print(text)

