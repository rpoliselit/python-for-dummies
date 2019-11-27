def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Dividor can NOT be ZERO.")
    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

print(calculate(15, 3, operator=divide))
