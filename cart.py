from product import Product


class Cart:

    def __init__(self):
        self.products = []

    def get_products(self):
        return self.products

    def set_products(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def disaplay_cart(self):
        for product in self.products:
            print(product.get_name())
    