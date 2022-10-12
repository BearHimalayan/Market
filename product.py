class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def display_product(self):
        print(f'product name: {self.name}, price: {self.price}')
