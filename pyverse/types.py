"""TYPES FILE"""
import struct
import uuid as p_uuid

class vector:
    """Vector type"""
    __name__ = "Vector"
    value = [0, 0, 0]
    def __init__(self, x, y, z=0):
        if type(x) == bytes:
            x, y, z = struct.pack_from('<fff', x, y)
            self.value = [x, y, z]
        else:
            self.value = [x, y, z]
        
    #X axis
    @property
    def x(self):
        return self.value[0]

    @x.setter
    def x(self, value):
        self.value[0] = value
    #W is copy of X
    @property
    def w(self):
        return self.value[0]

    @w.setter
    def w(self, value):
        self.value[0] = value
        
    #Y axis
    @property
    def y(self):
        return self.value[1]

    @y.setter
    def y(self, value):
        self.value[1] = value
    #H is copy of Y
    @property
    def h(self):
        return self.value[1]

    @h.setter
    def h(self, value):
        self.value[1] = value
        
    #Z axis
    @property
    def z(self):
        return self.value[2]

    @z.setter
    def z(self, value):
        self.value[2] = value
    #D is copy of Z
    @property
    def d(self):
        return self.value[2]

    @d.setter
    def d(self, value):
        self.value[2] = value
        
    #Mathematical functions
    def __add__(self, other):
        t = type(other)
        if t == vector:
            return vector(
                self.value[0] + other.value[0], 
                self.value[1] + other.value[1], 
                self.value[2] + other.value[2]
            )
        elif t == str:
            return ("<%f, %f, %f>"%(self.value[0],self.value[1],self.value[2]))\
                + other
        else:
            raise TypeError("Cannot add type <%s> to type <%s>!"
                % (type(self).__name__, type(other).__name__))
            
    def __radd__(self, other):
        t = type(other)
        if t == vector:
            return vector(
                other.value[0] + self.value[0], 
                other.value[1] + self.value[1], 
                other.value[2] + self.value[2]
            )
        elif t == str:
            return other \
                + ("<%f, %f, %f>" % (self.value[0],self.value[1],self.value[2]))
        else:
            raise TypeError("Cannot add type <%s> to type <%s>!"
                % (type(other).__name__, type(self).__name__))
                
    def __eq__(self, other):
        if type(other) == vector:
            if other.value[0] == self.value[0] && \
               other.value[1] == self.value[1] && \
               other.value[2] == self.value[2]:
                return True
        return False
                
    def __ne__(self, other):
        if type(other) == vector:
            if other.value[0] == self.value[0] && \
               other.value[1] == self.value[1] && \
               other.value[2] == self.value[2]:
                return False
        return True
                
    #Type conversion
    def __str__(self):
        return "<%f, %f, %f>" % (self.value[0],self.value[1],self.value[2])
        
    def __bytes__(self):
        return struct.pack('<fff', self.value[0], self.value[1], self.value[2])
        
#Same thing as vector except using doubles instead of floats
class vector3d(vector):
    def __init__(self, x, y, z=0):
        if type(x) == bytes:
            x, y, z = struct.pack_from('<ddd', x, y)
            self.value = [x, y, z]
        else:
            self.value = [x, y, z]
    def __bytes__(self):
        return struct.pack('<ddd', self.value[0], self.value[1], self.value[2])
        

class rotation:
    """Rotation type"""
    __name__ = "Rotation"
    value = [0, 0, 0, 0]
    def __init__(self, x, y, z=0, s=0):
        if type(x) == bytes:
            x, y, z, s = struct.pack_from('<ffff', x, y)
            self.value = [x, y, z, s]
        else:
            self.value = [x, y, z, s]
        
    #X axis
    @property
    def x(self):
        return self.value[0]

    @x.setter
    def x(self, value):
        self.value[0] = value
        
    #Y axis
    @property
    def y(self):
        return self.value[1]

    @y.setter
    def y(self, value):
        self.value[1] = value
        
    #Z axis
    @property
    def z(self):
        return self.value[2]

    @z.setter
    def z(self, value):
        self.value[2] = value
        
    #S axis
    @property
    def s(self):
        return self.value[3]

    @s.setter
    def s(self, value):
        self.value[3] = value
        
    #W axis, basically alias of s axis
    @property
    def w(self):
        return self.value[3]

    @w.setter
    def w(self, value):
        self.value[3] = value
        
    #Mathematical functions
    def __add__(self, other):
        t = type(other)
        if t == vector:
            return vector(
                self.value[0] + other.value[0], 
                self.value[1] + other.value[1], 
                self.value[2] + other.value[2], 
                self.value[3] + other.value[3]
            )
        elif t == str:
            return ("<%f, %f, %f, %f>"% \
                (self.value[0],self.value[1],self.value[2],self.value[3]))\
                + other
        else:
            raise TypeError("Cannot add type <%s> to type <%s>!"
                % (type(self).__name__, type(other).__name__))
            
    def __radd__(self, other):
        t = type(other)
        if t == vector:
            return vector(
                other.value[0] + self.value[0], 
                other.value[1] + self.value[1], 
                other.value[2] + self.value[2], 
                other.value[3] + self.value[3]
            )
        elif t == str:
            return other \
                + ("<%f, %f, %f, %f>"% \
                (self.value[0],self.value[1],self.value[2],self.value[3]))
        else:
            raise TypeError("Cannot add type <%s> to type <%s>!"
                % (type(other).__name__, type(self).__name__))
    
    def __mul__(self, other):
        print("__MUL__ IS NOT YET SUPPORTED!")
        return self
        
    def __eq__(self, other):
        if type(other) == rotation:
            if other.value[0] == self.value[0] && \
               other.value[1] == self.value[1] && \
               other.value[2] == self.value[2] && \
               other.value[3] == self.value[3]:
                return True
        return False
                
    def __ne__(self, other):
        if type(other) == rotation:
            if other.value[0] == self.value[0] && \
               other.value[1] == self.value[1] && \
               other.value[2] == self.value[2] && \
               other.value[3] == self.value[3]:
                return False
        return True
                
    #Type conversion
    def __str__(self):
        return "<%f, %f, %f, %f>"\
            % (self.value[0],self.value[1],self.value[2],self.value[3])
                                                                
    def __bytes__(self):                                        
        return struct.pack('<ffff',\
            self.value[0], self.value[1], self.value[2] self.value[3])

#It's the same thing, aliased for convienience
class quaternion(rotation):
    pass
#Sort of the same thing
class vector4d(rotation):
    pass

class uuid:
    """We rely on the built in UUID system, but we create our own structure
    as to allow mutation and custom features without overloading the current"""
    value = p_uuid.UUID(bytes=b"\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0")
    def __init__(self, inp, offset=0):#%0.2X
        t =  type(inp)
        if t == bytes:
            self.value = inp[0+offset:16+offset]
            if len(self.value) != 16:
                raise Exception("UUID is invalid!")
            self.value = p_uuid.UUID(bytes=self.value)
            
        elif t == str:
            if len(str) != 37:
                raise Exception("UUID is invalid!")
            self.value = p_uuid.UUID(inp)
            
    def __str__(self):
        return str(self.value)
        
    def __bytes__(self):                                        
        return self.value.bytes
        
class variable1:
    len = 0
    value = b""
    def __init__(self, inp, offset=0):
        self.len, = struct.unpack(">B", inp)
        self.value = inp[offset+1:offset+self.len]
        
    def __str__(self):
        return self.value.decode()
        
    def __bytes__(self):                                        
        return self.value
        
    def __len__(self):                                        
        return self.len
        
class variable2:
    len = 0
    value = b""
    def __init__(self, inp, offset=0):
        self.len, = struct.unpack(">H", inp)
        self.value = inp[offset+2:offset+self.len]
        
    def __str__(self):
        return self.value.decode()
        
    def __bytes__(self):                                        
        return self.value
        
    def __len__(self):                                        
        return self.len
        
class bool:
    value = False
    def __init__(self, inp, offset=0):
        tmp, = struct.unpack(">b", inp)
        if tmp == 0:
            self.value = False
        else:
            self.value = True
        
    def __str__(self):
        if self.value == 0:
            return "False"
        return "True"
        
    def __bytes__(self):                                        
        return struct.pack(">b",self.value!=0)
        
    def __len__(self):                                        
        return 1
        
class IPADDR:
    value = [0,0,0,0]
    def __init__(self, inp, offset=0):
        tmp = struct.unpack(">BBBB", inp)
        self.value = [tmp[0],tmp[1],tmp[2],tmp[3]]
        
    def __str__(self):
        return "%i.%i.%i.%i"%(self.value[0],self.value[1],self.value[2],self.value[3])
        
    def __bytes__(self):                                        
        return struct.pack(">BBBB",self.value[0],self.value[1],self.value[2],self.value[3])
        
    def __len__(self):                                        
        return 4
        
class IPPORT:
    value = 0
    def __init__(self, inp, offset=0):
        tmp = struct.unpack(">H", inp)
        self.value = [tmp[0],tmp[1],tmp[2],tmp[3]]
        
    def __str__(self):
        return "%i"%self.value
        
    def __bytes__(self):                                        
        return struct.pack(">H",self.value)
        
    def __len__(self):                                        
        return 2
        
if __name__ == __main__:
    #TESTBED
    print(vector(1,2,3) + "Test")