import threading
import time
class myThread (threading.Thread):#super
   def __init__(self, name): #constrctor
      threading.Thread.__init__(self)
      self.name = name

   def run(self): #this is thread function
      print ("Starting " + self.name)
      for count in range(1,6):
         time.sleep(5)
         print ("Thread name: {} Count: {}".format ( self.name, count ))
      print ("Exiting " + self.name)

# Create new threads
thread1 = myThread("Aniv1")
thread2 = myThread("Aniv2")

# Start new Threads
thread1.start()  # run 
thread2.start()  # run
thread1.join()
thread2.join()
print ("Exiting Main Thread")