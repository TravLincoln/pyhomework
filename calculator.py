def calculator(num1,num2,operator):
    if operator =='+':
        return float(num1) + float(num2)

    elif operator == '-':
        return float(num1) -  float(num2)

    elif operator == '*':
        return float(num1) * float(num2)
   
    elif operator == '/':
        return float(num1) / float(num2) if float(num2) != 0 else 0

    elif operator == "**":
        return float(num1)** float(num2)

    else:
        return False

def parse_input():
    num1,operator,num2 = input("Enter equation: ").split()
    print(calculator(num1,num2,operator))
