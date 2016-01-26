#online friends

import sleekxmpp
import logging

def session_start(event):
    chatbot.send_presence()
    print 'session started'

jid = 'kartikjagdale@chat.facebook.com'
<<<<<<< HEAD
password = '@nn3.Fr@nk'
=======
password = 'yourpassword'
>>>>>>> 59211825f79ddf0782e9fdeaa793240768697909
server = ('chat.facebook.com',5222)

chat = sleekxmpp.ClientXMPP(jid,password)
chat.add_event_handler('session_start',session_start)
#chat.add_event_handler('message',message)
chat.auto_reconnect = True
chat.connect(server)
chat.process(block=True)
print 'connected'
