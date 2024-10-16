from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class CoffeeMachine:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.money_machine = MoneyMachine()
        self.drinks_menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.coffee_types = self.drinks_menu.get_drink_names()
        self.choice = ''

    def _get_user_choice(self):
        ''' Gets a choice from user. Validates the input and keeps asking for
        user inputs till user enters a valid input. '''
        coffee_str = self.drinks_menu.get_items()
        valid_choices = self.coffee_types + ['off', 'report']
        self.choice = input(f"What would you like? ({coffee_str}): ").lower()
        while self.choice not in valid_choices:
            print(f"Please choose one of the following options:\n{coffee_str}\n")
            self.choice = input(f"What would you like? ({coffee_str}): ").lower()

    def _order_cofee(self):
        ''' Method to proces coffee orders from users. It first checks availability of resources.
        If resources are available, then asks user to enter coins. If user has entered enough coins.
        It returns change and serves coffee to the user.'''
        drink = self.drinks_menu.find_drink(self.choice)
        if self.coffee_maker.is_resource_sufficient(drink):
            if self.money_machine.make_payment(drink.cost):
                self.coffee_maker.make_coffee(drink)

    def process_order(self):
        ''' Main method for executing coffee machine functionalities. 
        Based on the user input, it prints report showing the resources and money,
        orders coffee or turns off the machine when user enters 'off' keyword. '''
        while self.choice != 'off':
            self._get_user_choice()
            if self.choice == 'report':
                self.coffee_maker.report()
                self.money_machine.report()
            elif self.choice in self.coffee_types:
                self._order_cofee()
            elif self.choice == 'off':
                print('Turning off the coffee machine.')


def main():
    coffee = CoffeeMachine()
    coffee.process_order()


if __name__ == "__main__":
    main()
