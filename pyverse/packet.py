import struct
class packet:
    """Load a packet"""
    #Body byte data, incase we need it
    bytes = b""
    body = {}
    
    #Flags
    flags = 0
    zero_coded = 0
    reliable = 0
    resent = 0
    ack = 0
    
    def __init__(self, msg_table, bytes):
        """Read an entire packet"""
        #Load in the header data
        self.flags, self.sequence, self.extra_bytes = \
            struct.unpack_from(">BiB", bytes[:6])
            
        #Unpack the flags
        self.zero_coded = (self.flags&0x10 == 16)
        self.reliable = (self.flags&0x10 == 16)
        self.resent = (self.flags&0x10 == 16)
        self.ack = (self.flags&0x10 == 16)
        
        if self.zero_coded:
            self.bytes = zerocode.decode(bytes[6+self.extra_bytes:])
        else:
            self.bytes = bytes[6+self.extra_bytes:]
            
        self.body = message(msg_table, self.bytes, {
            "zero_coded": self.zero_coded,
            "reliable": self.reliable,
            "resent": self.resent,
            "ack": self.ack
        })

class message:
    id = 0
    frequency = 1
    bytes = b""
    flags = {
        "zero_coded": False,
        "reliable": False,
        "resent": False,
        "ack": False
    }
    def __init__(self, msg_table, bytes=None, flags=None):
        if bytes:
            self.loadBytes(bytes)
        if flags:
            self.flags = flags
        
    def loadBytes(self, bytes):
        #Find the magic number
        if bytes[0] > 0xfe:
            self.frequency = 2
            self.id, = struct.unpack_from(">H", bytes[:2])
            self.bytes = bytes[2:]
            if self.id > 0xfffe:
                self.id, = struct.unpack_from(">I", bytes[:4])
                self.frequency = 4
                self.bytes = bytes[4:]
        else:
            self.id = bytes[0]
            self.bytes = bytes[self.frequency:]
            
        for i in a:
            msgTemplate["RezRestoreToWorld"].children
    
    def fromStruct(self, data):
        self.pies = []
