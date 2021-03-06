def readCurrency(txt):
    """
    -> Number validation.
    :txt: message printed before number validation.
    :return: a float number.
    """
    while True:
        try:
            user_input = input(txt).strip()
            if '.' in user_input or user_input.isnumeric():
                p = float(user_input)
                break
            elif ',' in user_input:
                p = float(user_input.replace(',','.'))
                break
            else:
                print('ERROR! This is not a valid number.')
        except ValueError:
            print('ERROR! Try a number.')
    return p
