import _thread
import time
#single thread main
def printdate():
   print('today')

printdate()
# Define a function for the thread

def print_time( threadName, delay):  #running
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
      #end 
def sayMessage(threadName,delay):
   i=0
   while(i<3):
      i=i+1
      time.sleep(delay)
      print('welcome to threads {} {}'.format(threadName,delay))
# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Producer", 2, ) )# new , ready
   _thread.start_new_thread( print_time, ("Consumer", 2, ) )
   _thread.start_new_thread(sayMessage,("child",1))
except:
   print ("Error: unable to start thread")

while 1:
   pass

