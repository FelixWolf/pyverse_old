from . import message

class template:
    def block(self, data):
        data = data[1:-1]
        i = 0
        l = len(data)
        blockDepth = 0
        tmp_data = ""
        params = []
        needsParams = 1
        children = []
        child_data = ""
        while i < l:
            if data[i] == "{":
                blockDepth = blockDepth + 1
            elif data[i] == "}":
                blockDepth = blockDepth - 1
            else:
                if blockDepth == 0:
                    if data[i] != "\n" and data[i] != "\t" and data[i] != " ":
                        tmp_data = tmp_data + data[i]
                        needsParams = 0
                    else:
                        tmp_data = tmp_data.strip()
                        if tmp_data != "":
                            params.append(tmp_data.strip())
                        tmp_data = ""
                
                if blockDepth > 0:
                    child_data = child_data + data[i]
                elif blockDepth == 0 and child_data != "":
                    children.append(self.block(child_data))
                    child_data = ""
            
            i = i + 1
        return block(params, children)
        
    messages = {}
    
    def __init__(self, src=None):
        #Allow user to give us a data if they wish
        data = ""
        if src == None:
            #Default function
            f = open(os.path.dirname(os.path.abspath(__file__))+
                "/message_template.msg", "r")
            data = f.read()
            f.close()
        elif type(src) == str:
            #It's a string
            data = src
        else:
            #File?
            try:
                #file.
                data = src.read()
            except Exception:
                #wut?
                raise Exception("Expected type NoneType, Str, or "+ \
                    "File handle, recieved %s."%type(src))
        
        i = 0
        l = len(data)
        isCommented = 0
        blockDepth = 0
        tmp_data = ""
        while i < l:
            #Handle comments
            if data[i] == "/": #start comment
                if data[i+1] == "/":
                    isCommented = 1
            
            if not isCommented: #Stop comments from being read 
                    
                if data[i] == "{":
                    blockDepth = blockDepth + 1
                    
                if blockDepth > 0:
                    tmp_data = tmp_data + data[i]
                elif blockDepth == 0 and tmp_data != "":
                    tmp = self.block(tmp_data)
                    if tmp.params[2][0:2] == "0x":
                        tmp.params[2] = int(tmp.params[2], 0)
                    else:
                        tmp.params[2] = int(tmp.params[2])
                        
                    if tmp.params[1] == "Medium":
                        tmp.params[2] = tmp.params[2] + 0xff00
                    elif tmp.params[1] == "Low":
                        tmp.params[2] = tmp.params[2] + 0xFFFF0000
                    elif tmp.params[1] == "Fixed":
                        tmp.params[2] = tmp.params[2] + 0xFFFFFF00
                    
                    self.messages[tmp.params[2]] = tmp
                    self.messages[tmp.params[0]] = tmp
                    tmp_data = "" 
                    
                if data[i] == "}":
                    blockDepth = blockDepth - 1
            if data[i] == "\n": #end comment
                isCommented = 0
                    
            i = i + 1

def getMessages():
    data = template().messages
    return data
    #packet.message()