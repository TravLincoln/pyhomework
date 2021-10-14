def tripler(func):                  #start of tripler function
    def wrapper_do_thrice():        #thrice decorator created
        func()                      #calls function once    
        func()                      #calls function twice
        func()                      #calls function thrice
    return wrapper_do_thrice        #return function called three times

