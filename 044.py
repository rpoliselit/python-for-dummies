"""
Make a program that calculates the
value to be paid for a product,
considering its NOMINAL PRICE and
PAYMENT CONDITIONS:
- cash: 10% off
- card (in one loop sum): 5% off
- card (2x): norminal price
- card (3x or more): 20% interest
"""
print('{:=^40}'.format(' PAYMENT CALCULATION '))
price = float(input('Enter the price: US$'))
print('-'*20,"""
1: Cash
2: In one loop sum (card)
3: Credit card (2x)
4: Credit card (3x or more)
""")
payment_form = int(input('Which one? ' ))
print('-=-'*20)

if payment_form == 1:
    print('US${:.2f} paid in cash.'.format(price*0.90))
elif payment_form == 2:
    print('US${:.2f} paid in one loop sum.'.format(price*0.95))
elif payment_form == 3:
    print('US${:.2f} paid in '.format(price), end = '')
    print('2x of US${:.2f} in credit card.'.format(price/2))
elif payment_form == 4:
    num = int(input('How many parcels? '))
    parcels = price * 1.20 / num
    print('US${:.2f} paid in '.format(price*1.20), end = '')
    print('{}x of US${:.2f} in credit card.'.format(num,parcels))
else:
    print('Payment canceled!')
