REQ_FILE_SEND  = 0x01
REP_FILE_SEND  = 0x02
FILE_SEND_DATA = 0x03
FILE_SEND_RES  = 0x04

NOT_FRAGMENTED = 0x00
FRAGMENTED = 0x01

NOT_LASTMSG = 0x00
LASTMSG = 0x01

ACCEPTED = 0x00
DENIED = 0x01

FAIL = 0x00
SUCCESS = 0x01

class ISerializable:
    def GetBytes(self):
        pass

    def GetSize():
        pass

class Message(ISerializable):
    def __init__(self):
        self.Header = ISerializable()
        self.Body = ISerializable()
        
    def GetBytes(self):
        buffer = bytes(self.GetSize())

        header = self.Header.GetBytes()
        body = self.Body.GetBytes()

        return header + body

    def GetSize(self):
        return self.Header.GetSize() + self.Body.GetSize()