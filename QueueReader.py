import threading, queue
import time
import Keys as config
import sys, traceback

from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)

#Thread-safe collection
from queue import Queue 

def ProcessMessage(message, queue):

    try:
        
        print(f"Running {message.id}")

        #Add on value to queue
        queue.put(message.id)
        
        print (message.content)
        time.sleep(20)

        #when finish, remove process
        queue.get()
        
        print(f"Finish {message.id}")
    except Exception:        
        print(f"Error on {message.id}")
        traceback.print_exc(file=sys.stdout)
        queue.get()

#Azure Queue
queue_client = QueueClient.from_connection_string(config.queueConnString, config.queueName)

q = Queue()
while(True):
    #Checks every 5 seconds
    time.sleep(5)
    try:
        messages = queue_client.receive_messages(messages_per_page=3)
        for message in messages:
            if q.qsize()>=config.concurrentThreads:
                print(f"You reach the limit of queues on this server = {q.qsize()}" )
            else:
                #Call Thread
                x = threading.Thread(target=ProcessMessage, args=(message,q),daemon=True)
                x.start()
                queue_client.delete_message(message.id, message.pop_receipt)
    except Exception:
        print(f"Error on {message.id}")
        traceback.print_exc(file=sys.stdout)