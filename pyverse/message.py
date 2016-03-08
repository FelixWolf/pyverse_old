import os, struct

class frequency:
    high = 0
    medium = 1
    low = 2
    fixed = 4
    def __init__(self):
        pass

class block:
    name = ""
    paramOrder = []
    def __init__(self, name="", paramOrder=[]):
        self.name = name
        self.paramOrder = paramOrder
        
    def __bytes__(self):
        result = b""
        for param in paramOrder:
            val = getattr(self, param[0])
            
            if param[1] == "Null":
                result = result + b"\x00"
            elif param[1] == "Fixed":
                result = result + bytes(val)
            elif param[1] == "Variable":
                if type(val) == bytes:
                    if param[2] == "1":
                        result = result + struct.pack("<B", len(val)) + val
                    elif param[2] == "2":
                        result = result + struct.pack("<H", len(val)) + val
                else: #Suspect it is a variable type, which already has length
                    result = result + bytes(val)
            elif param[1] == "U8":
                result = result + struct.pack("<B", val)
            elif param[1] == "U16":
                result = result + struct.pack("<H", val)
            elif param[1] == "U32":
                result = result + struct.pack("<I", val)
            elif param[1] == "U64":
                result = result + struct.pack("<Q", val)
            elif param[1] == "S8":
                result = result + struct.pack("<b", val)
            elif param[1] == "S16":
                result = result + struct.pack("<h", val)
            elif param[1] == "S32":
                result = result + struct.pack("<i", val)
            elif param[1] == "S64":
                result = result + struct.pack("<q", val)
            elif param[1] == "F32":
                result = result + struct.pack("<f", val)
            elif param[1] == "F64":
                result = result + struct.pack("<d", val)
            elif param[1] == "LLVector3":
                result = result + bytes(val)
            elif param[1] == "LLVector3d":
                result = result + bytes(val)
            elif param[1] == "LLVector4":
                result = result + bytes(val)
            elif param[1] == "LLQuaternion":
                result = result + bytes(val)
            elif param[1] == "LLUUID":
                result = result + bytes(val)
            elif param[1] == "BOOL":
                result = result + bytes(val)
            elif param[1] == "IPADDR":
                result = result + bytes(val)
            elif param[1] == "IPPORT":
                if type(val) == int:
                    result = result + struct.pack("<H", val)
                else:
                    result = result + bytes(val)
            #End param if
        #End for loop
        
        return result


class message:
    name = ""
    id = 0
    frequency = 0
    trusted = False
    encoded = False
    blockOrder = []
    def __init__(self, n="", i=0, f=0, t=False, e=False, o=[]):
        self.name = n
        self.id = i
        self.frequency = f
        self.trusted = t
        self.encoded = e
        self.blockOrder = o
    
    def __bytes__(self):
        result = b""
        
        #Set the message ID byte(s)
        if self.frequency == frequency.fixed:
            result = struct.pack(">I", self.id + 0xFFFFFF00)
        elif self.frequency == frequency.low:
            result = struct.pack(">I", self.id + 0xFFFF0000)
        elif self.frequency == frequency.medium:
            result = struct.pack(">H", self.id + 0xff00)
        elif self.frequency == frequency.high:
            result = struct.pack(">B", self.id)
        
        #Pack the body
        for blk in self.blockOrder:
            val = getattr(self, blk[0])
            
            #If it is a variable, we need the count
            if blk[1] == "Variable":
                #Allows for just one as a non-list
                if type(val) == list:
                    result = result + struct.pack(">B", len(val))
                else:
                    result = result + b"\x01" #We already know how many, one
            
            #Pack each value
            if type(val) == list:
                #for each, since it is a list
                for subblk in val:
                    result = result + bytes(subblk)
            else:
                #Just one
                result = result + bytes(getattr(self, blk[0]))
        
        return result
