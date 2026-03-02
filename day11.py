import random

def del_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(com_score, u_score):
    if com_score == u_score:
        return "DRAW"
    elif 21 > u_score > com_score:
        return f"your score is {u_score} and computer score is {com_score}, you WON !"
    elif computer_score > 21:
        return "Computer WON !"

user_cards = []
computer_cards =[]
computer_score = -1
user_score = -1
is_game_over = False
for _ in range(2):
    user_cards.append(del_card())
    computer_cards.append(del_card())


while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_score}")
    if user_score == 0 and computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user = input("do you want to draw another card 'yes' and no ")
        if user == "yes":
            user_cards.append(del_card())
        else:
            is_game_over = True
        # elif user ==  'no':
        #     if computer_score < 17:
        #         computer_cards.append(del_card())
        #         if
while computer_score < 17:
    computer_cards.append(del_card())
    computer_score = calculate_score(computer_cards)

print(f"your final score is {user_score}")
print(f"computer final score is {computer_score}")

print(compare(computer_score, user_score))




# user = input("do you want to add another card if yes then press 'yes'")

# while(user == "yes"):
#     user_cards.append(del_card())
# print(sum(user_cards))













    # has_user_blackjack = 10 in user_cards and 11 in user_cards
    # has_comp_blackjack = 10 in computer_cards and 11 in computer_cards
    #
    # if has_user_blackjack:
    #     print("User wins!")
    # elif has_comp_blackjack:
    #     print("computer wins!")
    #
    # if score_user > 21:
    #     has_user_blackjack = False
    #

#
# def over_21():
#     user = input("do you want to get another card, draw ? enter 'yes'")
#     if(user == "yes"):
#         for _ in range(1):
#             user_cards.append(del_card)
#         sum(user_cards)
#
#     for _ in range(1):
#         computer_cards.append(del_card)
#         user_result = sum(computer_cards)
#
#     result_comp = sum(computer_cards)
#     if (result_comp > 21):
#         print(f"You wim, compuer score is over 21 {result_comp}")
#     elif(user_result == result_comp):
#         print(f"it is draw, computer score is {result_comp} "
#               f"and user's result is {user_result}")
#     elif(user_result > result_comp):
#         print(f"you win {user_result}")
#     else:
#         print(f"You lost,  {result_comp} and user result is {user_result}")

    # print(score_user)
    # print(score_computer)
# print(computer_cards)
# print(user_cards)

