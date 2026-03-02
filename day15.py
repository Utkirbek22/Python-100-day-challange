
from day15menu import MENU
from day15menu import resources

MONEY = 0

def report():
    print(f"water: {resources["water"]} ml")
    print(f"milk: {resources["milk"]} ml")
    print(f"coffe: {resources["coffee"]}g" )
    print(f"money: ${MONEY} ")

def sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def process_coins():
    print("insert the coins")
    total = int(input("how many quarters ?: ")) * 0.25
    total += int(input("how many dimes ?: ")) * 0.1
    total += int(input("how many nickles ?: ")) * 0.05
    total += int(input("how many pennies ?: ")) * 0.01
    return total

def is_transaction_successfull(money_recieved, drink_cost):
    global MONEY
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost)
        print(f"here is your change{change}")
        MONEY += drink_cost
        return True
    else:
        print("Sorry, that is not enough momey, Money refunded! ")
        return False

def preparation_coffee(drink_name,products):
    for item in products:
        resources[item] -= products[item]
    print(f"here is your {drink_name} ☕")

    # while user_insert_money != 100:
    #     user_insert_money = int(input("insert the money"))
    #     total += user_insert_money
    # print(f"total coins amount is {total}")
    # if total < drink["cost"]:
    #     print("Sorry, that is not enough momey, Money refunded! ")
    # elif total == drink["cost"]:
    #     total += MONEY
    # elif total > drink["cost"]:
    #     change = total - drink["cost"]
    #     return f"Here is your change {change}"



is_on = True
while is_on:
    user = input("“What would you like? (espresso/latte/cappuccino): ")
    if user == "off":
        is_on = False
    elif user == "report".lower():
        report()
    else:
        drink = MENU[user]
        if sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successfull(payment, drink["cost"]):
                preparation_coffee(user, drink["ingredients"])

















#
# elif user_coffee == "report".lower():
#     for key, value in resources.items():
#         print(f"{key}: {value}")