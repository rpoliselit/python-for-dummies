class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + ' - franchise')

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock price: {}".format(store.name,int(store.stock_price()))

store_1 = Store("Test")
store_2 = Store("Amazon")
store_2.add_item('Keyboard',160)

f_1 = Store.franchise(store_1)
f_2 = Store.franchise(store_2)
print(f"{f_1}\n{f_2}")

sd_1 = Store.store_details(f_1)
sd_2 = Store.store_details(store_2)
print(f"{sd_1}\n{sd_2}")
