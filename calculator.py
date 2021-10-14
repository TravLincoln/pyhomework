def calculator(num1,num2,operator):          #start of calculator function
    
    if operator =='+':                       #if user presses plus sign, add num1 and num2
        return float(num1) + float(num2)

    elif operator == '-':                    #or else if the user presses the subract sign, subtract num1 from num2
        return float(num1) -  float(num2)

    elif operator == '*':                    #or else if user preses multiply sign, multiply num1 by num2
        return float(num1) * float(num2)
   
    elif operator == '/':                    #or else if user........ division...., divide num1 by num2
        return float(num1) / float(num2) if float(num2) != 0 else 0
    
    elif operator == '//':                   #or else if user. floor division, divide num1 by num2 and round lowest num
        return float(num1) // float(num2) if float(num2) !=0 else 0

    elif operator == '**':                   #or else if user... exponent, raise num1 by exponent num2
        return float(num1)** float(num2)

    else:                                    #otherwise, return false
        return False

def parse_input():                           #divides program into smaller pieces of code to analyze correct syntax
    num1,operator,num2 = input("Enter equation: ").split()  #split takes each argument and seperates them individually
    print(calculator(num1,num2,operator))                   
