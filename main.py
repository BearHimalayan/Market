from menu import Menu
from product import Product
from pocket import Pocket
from cart import Cart
from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', pocket=pocket.get_balance(), cart=cart.get_products(), menu=menu.get_products())

@app.route("/buy_product/")
def buy_product():
    return render_template('index.html', pocket=pocket.get_balance(), cart=cart.get_products(), menu=menu.get_products())


pocket = Pocket(100)
cart = Cart()
menu = Menu()
menu.add_product(Product('fish', 5))
menu.add_product(Product('Meat', 160))
menu.add_product(Product('Cake', 6))
menu.add_product(Product('Orange', 1))
menu.add_product(Product('Apple', 0.5))


# while True:

#     pocket.display_balance()
#     menu.display_products()
#     choice = input('What product do you want?')
#     product = menu.get_product(choice)
#     cart.add_product(product)
#     product_price = product.get_price()
#     pocket.spend_balance(product_price)
#     cart.disaplay_cart()


