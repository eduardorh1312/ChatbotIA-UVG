from fbchat import Client, log
from fbchat.models import *

class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        
        if author_id != self.uid:

            reply = "Hola putito soy un bot y voy a dominar el mundo"
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)


client = EchoBot("eduardorh1312@gmail.com", "chatbot")
client.listen()
