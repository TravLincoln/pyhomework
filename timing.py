import time                     #import time class from python library

def calculate_time(tester):     #calculate time function created with tester() decorator
    def wrapper():              #start of decorator
        start = time.time()
        tester()                #decorator called
        end = time.time()
        total= end - start
        print("Total time {}".format(total)) #calculate total time by end-strart time .format() allows variable subs
    return wrapper

def func_time():                #calculates time with 2 second wait
    time.sleep(2)
    
func_time = calculate_time(func_time) #function created where time is calulated with 2 second wait
func_time()                         #runs command

