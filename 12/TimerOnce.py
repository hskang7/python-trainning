import threading
import datetime

def function_a():    
    print("Timer expired")
    print(datetime.datetime.now())
    
print(datetime.datetime.now())
threading.Timer(10, function_a).start()