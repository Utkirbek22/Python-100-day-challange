from mimetypes import guess_type
from random import randint
num = randint(1,100)

EASY_SHOT = 10
HARD_SHOT = 5

def check_answer(user_guess, actual_number):
    if user_guess > actual_number:
        print("Too high")
    elif user_guess < actual_number:
        print("too low")
    else:
        print(f"You got it. the answer is {actual_number}")

def set_difficulty():
    level = input("choose the the difficulty easy or hard: ")
    if level == "easy":
        return EASY_SHOT
    else:
        return HARD_SHOT

print("Welcome to the game")
print(f"that is correct answer {num}")
turns = set_difficulty()
guess = 0
while(guess != num):
    guess = int(input("make a guess: "))
    check_answer(guess, num)
    print(f"You have {turns} attampts remaining to guess number")
    if turns == 0:
        print("you run out of guesing, you lost")
        break
    turns -= 1


# import random
#
# print("Welcome to game")
#
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# random_number = random.choice(numbers)
# easy_shots = 3
# hard_shots = 5
# user = input("choose the game of the level easy or hard: ").lower()
# if user == "easy":
#     while easy_shots >= 1:
#         print(f"You have {easy_shots} attempts remaining to guess th number")
#         guessing_number = int(input("make a guess: "))
#         if random_number == guessing_number:
#             print("you guessed it correctly")
#             break
#         elif guessing_number > random_number:
#             print("too high \n guess again")
#         elif guessing_number < random_number:
#             print("too low \n guess again")
#         else:
#             print("you lost")
#         easy_shots -= 1




