import time 

def calculate_time(time):
    return f"Total time {time}"

def timefunc(totaltime):
    return totaltime(time.time())
time.sleep(2)
    
print(calculate_time(time))
