"""
Make a script that reads a temperature in Celsius degree
and returns the temperature into Fahrenheits degree.
"""

def conv(T_Celsius):
    T_Fahrenheits = (212-32) / (100-0) * T_Celsius + 32
    return T_Fahrenheits

temp = float(input('Type a temperature in Celsius degree: '))

print('The temperature in Fahrenheits scale is {:.1f}.'.format(conv(temp)))
