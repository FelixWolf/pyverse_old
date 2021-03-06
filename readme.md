**This is hanging around for legacy purposes, see https://github.com/FelixWolf/pyverse for the newer code**
Purpose
------
The purpose this is to provide a simple python API to connect to Second Life.<br/>
While [PyOGP](http://wiki.secondlife.com/wiki/PyOGP) already exists, to my experience
the docs are missing/poorly written and it includes a lot more than just a bot.

This aims to be simple, and easy to use with minimal packet construction.

Example of use
------
**WARNING**: This is a proof of concept, and is not actually functional.<br/>
This is what this is aimed to be at the moment.
```python
import pyverse

messages = pyverse.message_template.getMessages()

#Initialize the session
session = pyverse.login(firstname, lastname, password, macAddr)

hello = messages.getMessage("ChatFromViewer")

#Fill out agent info
hello.AgentData.AgentID = session.agent.AgentID
hello.AgentData.SessionID = session.agent.SessionID

#We can safely pass integers and strings as these get transformed automatically
hello.ChatData.Message = "Hello, world!"
hello.ChatData.Type = 1
hello.ChatData.Channel = 0

#We can pass messages to sendMessage to construct it as a packet and send it in
#one go!
session.sendMessage(hello)
```

Current status
------
zerocode.py (Fully implemented):
- bytes pyverse.zerocode.decode(bytes)
- bytes pyverse.zerocode.encode(bytes)
    
template.py (Partually implemented, needs to be rewritten):
- No extra info, no need to document because of being rewritten

message.py (Fully implemented?):
- No extra info at the moment

packet.py (Junk code, needs to be rewritten(MAYBE?)):
- No extra info at the moment

Contribution
------
Think you can help pyverse grow and become better? Commit your changes to the
main branch and help us out! (Feel free to add your name/info to
contributors.txt while you are at it too!)

License
------
I'll add the license in the code later, it's under the MIT license.

>The MIT License (MIT)
>
>Copyright (c) 2016 pyverse contributors(See contributors.txt)
>
>Permission is hereby granted, free of charge, to any person obtaining a copy
>of this software and associated documentation files (the "Software"), to deal
>in the Software without restriction, including without limitation the rights
>to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
>copies of the Software, and to permit persons to whom the Software is
>furnished to do so, subject to the following conditions:
>
>The above copyright notice and this permission notice shall be included in all
>copies or substantial portions of the Software.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
>IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
>FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
>AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
>LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
>OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
>SOFTWARE.

Copyrights and disclaimers
------
Pyverse and it's contributors are not endorsed, affiliated, or sponsored by
Linden Lab, the creators of Second Life, or Second Life it's self.<br/>
Second Life is registered trademark of Linden Lab, Inc.
