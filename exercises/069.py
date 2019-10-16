"""
Make a program that name and price of
various goods. The program should
ask if the user wants to continue.
At the end, show:
[1] What is the total amount spent on the purchase?
[2] How many products cost more than $ 1000.
[3] The cheapest product name.
"""

print(f"""{'='*30}\n{'ORDER':^30}\n{'='*30}""")

check = expensive = cheaper = 0
while True:
    item = str(input('Item: ')).strip()
    price = float(input('Price: US$'))
    check += price
    if price > 1000:
        expensive += 1
    if price < cheaper or cheaper == 0:
        cheaper = price
        cheapest = item.title()
    ans = ' '
    while ans not in 'yn':
        ans = str(input('Continue? [y/n] ')).strip().lower()[0]
    if ans == 'n':
        break

print(f"""\nTotal: US${check:.2f}
Expensive itens: {expensive}
Cheaspest item: {cheapest}""")
