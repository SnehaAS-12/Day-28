#Define a subclass using threading.Thread class.

import threading
import time
exitFlag = 0
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Start " + self.name)
        print_time(self.name, 5, self.counter)
        print( "End " + self.name)
def print_time(threadName, counter, delay):
     while counter:
         if exitFlag:
             threadName.exit()
             time.sleep(delay)
             print("%s: %s" % (threadName, time.ctime(time.time())))
             counter -= 1
             
             
#Instantiate the subclass and trigger the thread.             
thr1 = myThread(1, "Thread_1", 1)
thr2 = myThread(2, "Thread_2", 2)
thr1.start()
thr2.start()
print("End of Thread")