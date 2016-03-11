import threading

count = 0

def OnTimer():    
    global count
    count += 1
    print(count)

    if count < 10:
        timer = threading.Timer(1, OnTimer)
        timer.start()

    #if count == 10:
    #    print("Canceling timer...")
    #    timer.cancel()

print("Starting timer...")
OnTimer()