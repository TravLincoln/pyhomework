import time 

def calculate_time(tester):
    def wrapper():
        start = time.time()
        tester
        end = time.time()
        total= end - start
        print("Total time {}".format(total))
    return wrapper

def func_time():
    time.sleep(2)
    
func_time = calculate_time(func_time)
func_time()

