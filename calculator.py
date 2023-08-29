def calculate(operation, x, y):
    if operation == 'addition':
        return x+y
    elif operation == 'subtraction':
        if x>y:
            return x-y
        else:
            return y-x
    elif operation == 'multiplication':
        return x*y
    elif operation == 'Division':
        return x/y