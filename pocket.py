from exceptions import NotEnoughMoney


class Pocket:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def add_balance(self, balance):
        self.__balance += balance

    def spend_balance(self, balance):
        if balance > self.__balance:
            raise NotEnoughMoney('You are poor Loser')
        else:
            self.__balance -= balance

    def display_balance(self):
        print(f'Your balance: {self.__balance}')

