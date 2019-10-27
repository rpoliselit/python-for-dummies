def fancy(func):
    def wrapper(x):
        print('-'*30)
        print(f"{func(x):^30}")
        print('-'*30)
    return wrapper

def create_pow(x):
    @fancy
    def pow(num):
        return x ** num
    return pow

pow_2 = create_pow(2)
pow_3 = create_pow(3)

pow_2(2)
pow_3(2)
