"""
Make a program that reads the car velocity.
If its over a limit of 120km/h, returns a
traffic ticket about US$50,00 fine,
and US$2,00 fine added per km excided.

Tip: some places there is about 5% of
tolerance in the measurement.
-------------------------------------------------------------------
NOTE: A crime without a victim is not a crime.
Prepare your crowbar!
Let's get cooper and make some gourmet electronic
components to sell at EletroGazetti.
"""

speed = float(input('Measured speed: '))

print('_'*20)

if speed > 120*(1.05):
    fine = 50 + 2 * (speed - 120)
    print('$$$$ Traffic ticket! $$$$')
    print('You were fined in US${:.2f}.'.format(fine))
else:
    print('You are clean!')
