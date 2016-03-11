import threading

def on_timer(count):    
    count += 1
    print(count)

    timer = threading.Timer(1, OnTimer, args=[count])
    timer.start()

    if count == 10:
        print("Canceling timer...")
        timer.cancel()

print("Starting timer...")
on_timer(0)