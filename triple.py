def tripler(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
@tripler
@decor
def num():
    return 10
print(num())

