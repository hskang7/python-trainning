import datetime
import threading

def check_time(curr_min):
    dt = datetime.datetime.now() 
    
    if curr_min != dt.minute:
        print(dt)
        curr_min = dt.minute
   
    threading.Timer(1, check_time, args=[curr_min]).start()

check_time(-1)