from day15 import drink
from day16money_machine import MoneyMachine
from day16coffee_maker import CoffeeMaker
from day16menu import Menu

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

coffe_maker.report()
money_machine.report()


is_on  = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would like to have {options}: ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)