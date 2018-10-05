def calculate(number1, number2, operator):
    check_number(number1)
    check_number(number2)
    check_argument_order(number1, number2, operator)
    if operator == 'add':
        result = add(number1, number2)
    return 'Result = ' + str(result)

def check_number(number):
    if len(str(number)) > 4:
        raise TypeError("Number {} is too long. Max 4 digits supported.".format(number))

def check_argument_order(arg1, arg2, arg3):
    if not type(arg1) in [int, float]:
        raise ValueError("Argument 1 must be either a whole or decimal number")
    if not type(arg2) in [int, float]:
        raise ValueError("Argument 2 must be either a whole or decimal number")
    if not type(arg3) == str:
        raise ValueError("Argument 3 must be the name of a operator such as 'add'")

def add(number1, number2):
    return(number1 + number2)
