#
# height = int(input("What is your height ?"))
# bill = 0
# if height > 120:
#     print("You are allowed to ride rollercaster")
#     age = int(input("What is your age"))
#
#     if age < 5:
#         bill = 5
#     elif age >= 5 and age < 12:
#          bill = 7
#     else:
#          bill = 10
#     photo = input("Would you like to have photos, if so press Y, otherwise X")
#
#     if photo == "Y":
#         bill += 3
#
#     print(f"Your final price is {bill}")
#
#
#
# else:
#     print("You aren't allowed!")


                                                          # Pizzza Task

#
# print("Welcome to Python Pizza Deliveries!")
# bill = 0
# size = input("WHat size of Pizza do you want ? S, M or L")
#
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25
#
#
# peperoni = input("Do you want pepperoni on your pizza ? Y or N: ")
# if peperoni == "Y":
#     if peperoni == "S":
#         bill += 2
#     else:
#         bill += 3
#
#
# extra_cheese = input("Add extra cheese for any pizze Y or N")
# if extra_cheese == "Y":
#     bill += 1
#
#
# print(f"Your final price is $ {bill}")
#
#



#  Treasure game

print("Welcome to Treasure Island \n Your mission is to find the treasure")

choice = input("Choose Left or Right")
if choice == "Right":
    print("You fell into a hole. Game Over.")
elif choice == "Left":
    swim_or_wait = input("swim or wait")
    if swim_or_wait == "swim":
        print("You got attacked by a Shark. Game Over.")
    elif swim_or_wait == "wait":
        which_door = input("Which door? red, blue or yellow")
        if which_door == "yellow":
            print("You win !")
        else:
            print("Lost. Game over!")


