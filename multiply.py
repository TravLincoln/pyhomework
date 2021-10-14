import math
def multiply_list(myList):
    
    res = float(1)
    for i in myList:
        res = float(res * i) 
    return float(res)
print(multiply_list([1,2,3,4]))
