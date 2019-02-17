#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 09:11:24 2019

@author: jeetu
"""

from fbchat import Client, log
from fbchat.models import *
import credential

class Jarvis(Client):
    def onMesssage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        self.markAsRead(author_id)
        
        log.info("Message {} from {} in {} ".format(message_object, thread_id,thread_type))
        msgText=message_object.text
        
        reply='hello world'
        
        if author_id!=self.uid:
            self.send(Message(text=reply),thread_id=thread_id,thread_type=thread_type)
            
        self.markAsDelivered(author_id,thread_id)
        
client = Jarvis(credential.email,credential.password)
client.listen( )
