# Python Queries Azure Storage Queues

This sample code shows how to interact with Azure Storage Queues on Python, using the https://pypi.org/project/azure-storage-queue package

It implements the following features:

1. Message Processing in Multiple Threads
2. Parallel Thread Control to avoid Server Overload
3. External Configuration File

## How To

1. Install the [requirements.txt](requirements.txt)

```
pip install -r requirements.txt
```

2. Update the  [Keys.py](Keys.py) with your keys


3.  Send multiple messages to Azure Storage Queue and observe the logs

```
PS C:\sc\pythonazurequeue> python .\QueueReader.py
Running c92feb0d-ebeb-4a2d-bbbd-7337e0863c6f
gaia5
Running dc712bad-d7d5-4037-91d8-51a9b5f4793f
gaia5
You reach the limit of queues on this server = 2
You reach the limit of queues on this server = 2
You reach the limit of queues on this server = 2
You reach the limit of queues on this server = 2
You reach the limit of queues on this server = 2
You reach the limit of queues on this server = 2
Finish c92feb0d-ebeb-4a2d-bbbd-7337e0863c6f
Finish dc712bad-d7d5-4037-91d8-51a9b5f4793f
Running 4f17840e-f10e-48ef-ae60-8464820a7a08
gaia5
Running 999331e8-a0e4-4f70-a166-3ac2ee7e09a5
gaia5
You reach the limit of queues on this server = 2
You reach the limit of queues on this server = 2
You reach the limit of queues on this server = 2
You reach the limit of queues on this server = 2
Finish 4f17840e-f10e-48ef-ae60-8464820a7a08
Finish 999331e8-a0e4-4f70-a166-3ac2ee7e09a5
````

## Important note:

When a listener gets a message, it´s become invisible to others about 30 seconds. In case of "Server Full" , the original message will return to the Queue.

When you explicit delete the message, this become unavailable to others.

