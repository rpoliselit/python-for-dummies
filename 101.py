"""
Make a program that has a factorial
function, which one gets to parameters:
1 - integer number
2 - logical value (optional) that indicates
whether the calculation process is shown or
not.
"""

def factorial(number, show=False):
    """
    -> Calculate the factorial of a integer number.
    :parameter number: Number to be calculate.
    :parameter show: (optional) Show the calculation process.
    :return: Factorial of number.
    """
    num = count = 1
    print('-'*40)
    while count <= number:
        num *= count
        if show == True:
            print(f'{count}', end = '')
            if count < number:
                print(end = ' x ')
            elif count == number:
                print(end = ' = ')
        count += 1
    return num


#Main program
#help(factorial)
print(factorial(5, show = True))
