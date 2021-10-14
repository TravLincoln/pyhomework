def do_thrice(func):
    def wrapper_do_thrice():
        func()
        func()
        func()
    return wrapper_do_thrice

