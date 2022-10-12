
from exceptions import ProductNotFound


class Menu:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)


    def display_products(self):
        for i in self.products:
            i.display_product()

    def get_product(self, product):
        for i in self.products:
            if i.get_name() == product:
                return i
        raise ProductNotFound

    def get_products(self):
        return self.products

