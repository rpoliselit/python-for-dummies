"""
Make a program that reads the wage of an employee,
and calculate its increase.

For wages up to US$1,250.00, calculate a increase of 15%.
For bigger wages the increase is of 10%.


NOTE: Wage calculates for month.
"""

wage = float(input('Enter the wage: '))

if wage <= 1250:
    new_wage = wage * 1.15
else:
    new_wage = wage * 1.10

print('The new wage is US${:.2f} per month.'.format(new_wage))
