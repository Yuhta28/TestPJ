# Python threading
import threading
from threading import *

# Our thread class
class MyThread(threading.Thread):
    def __init__(self,x):
        self.__x = x
        threading.Thread.__init__(self)

    def run(self):
        print(str(self.__x))

# Start 10 threads
for x in range(10):
    MyThread(x).start()

# Timed threads

def hello():
    print('hello world')

# Create thread
t = Timer(3.5, hello)

# Start thread after 10 seconds
t.start()