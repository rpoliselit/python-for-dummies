def currency(p):
    """
    -> Formats price.
    :p: price.
    """
    return f'U${p:.2f}'


def increase(p, r, f):
    """
    -> Increases a price in percentage.
    :p: price to be increased.
    :r: percentage to increase the price.
    :f: format as US$...
    :return: p*(1+r/100)
    """
    p *= (1 + r/100)
    return currency(p) if f is True else p


def decrease(p, r, f):
    """
    -> Decreases a price in percentage.
    :p: price to be decreased.
    :r: percentage to decrease the price.
    :f: format as US$...
    :return: p*(1-r/100)
    """
    p *= (1 - r/100)
    return currency(p) if f is True else p


def double(p, f=True):
    """
    -> Doubles the price.
    :p: price
    :f: format as US$...
    :return: 2*p
    """
    p *= 2
    return currency(p) if f is True else p


def half(p, f=True):
    """
    -> Cuts the price in half.
    :p: price
    :f: format as US$...
    :return: p/2
    """
    p /= 2
    return currency(p) if f is True else p


def summary(p, i, d):
    """
    -> Make a table of prices.
    :p: price
    :i: percentage to raise the price
    :d: percentage to lower the price
    """
    print('~'*40)
    print(f'{"VALUE SUMMARY":^40}')
    print(f'~'*40)
    print(f'{"Analized price:":.<20}{currency(p):.>20}')
    print(f'{"Double-price:":.<20}{double(p):.>20}')
    print(f'{"Half-price:":.<20}{half(p):.>20}')
    print(f'Increase of {i:2.0f}{"%:":.<6}{increase(p,i,True):.>20}')
    print(f'Reduction of {d:2.0f}{"%:":.<5}{decrease(p,d,True):.>20}')
    print(f'~'*40)
