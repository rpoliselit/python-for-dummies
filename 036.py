"""
Make a program to approve a bank logan
for the purchase of a property. The program
needs 'the price of property', 'the buyer's wage',
and 'loan time'.

Calculate the amount of the monthly installment
knowing that it can not exceed 30% of the salary,
or the loan is denied.
"""
print("Bank Loan Plans: my home, my life.")

price = float(input('How much is the property?\nUs$'))
wage = float(input('Enter the wage per month:\nUs$'))
years = float(input('How long do you intend to pay?\nYears: '))
months = years*12
provision = price / months

if provision > wage * 30 / 100:
    print('Funding DENIED!')
else:
    print('Funding APPROVED!')

print('The installment is US${:.2f} a month.'.format(provision))
