import math
def multiply_list(myList): #start of function
    
    res = 1                 #sets base for list to be multiplied by
    for i in myList:        #start of loop
        res = float(res * i)    #as long as there are elements in list, keep multipying
    return int(res)     #returns multiplied list
print(multiply_list([1,2,3,4]))
