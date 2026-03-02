import random

computer_cards = []
user_cards = []
total_comp = -1
total_user = -1
def del_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return  card

def calculate_score(cards):
    sum(cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and  sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "it is draw"
    elif 0 in user_cards or u_score > 21:
        return "Computer wins"
    elif 0 in computer_cards or c_score > 21:
        return "User wins"
    elif u_score > c_score and u_score <= 21:
        return f"User wins {u_score}"
    else:
        return f"comp wins {c_score}"

for _ in range(2):
    card_random = del_card()
    computer_cards.append(card_random)
    user_cards.append(card_random)

is_game_over = False
while not is_game_over:
    total_user =  calculate_score(user_cards)
    total_comp = calculate_score(computer_cards)

    print(f"user first score is {user_cards} and total score is {total_user}")
    print(f"computer first card is {computer_cards[0]} ")


    if total_user == 0 or total_comp == 0 or total_user > 21:
        is_game_over = True
    else:
        user_choice = input("do you want to draw y or n").lower()
        if user_choice == "y":
            user_cards.append(del_card())
        else:
            is_game_over = True

while total_comp != 0 and total_comp < 17:
    computer_cards.append(del_card())
    total_comp = calculate_score(computer_cards)

print(f"your final hands is {user_cards} amd score is {total_user}")
print(f"computer's final hand is {computer_cards} and score is { total_comp}")
print(compare(total_user, total_comp))
    # sum(computer_cards)
    # sum(user_cards)
    # return sum(score)
    # if 21 == score:
    #     return 0
    # elif score > 21:
    #     score.remove(11)
    #     score += 1




# def calculate_score(score):
#     sum(computer_cards)
#     sum(user_cards)
#     if 11 in computer_cards or 11 in user_cards:
#         return
#     elif 11 in computer_cards or 11 in user_cards and  score > 21:
#         score.remove(11)
#         score += 1
#
# result = calculate_score()
# if 11 in computer_cards or 11 in user_cards and result > 21:
#     print("Game over")
# else:
#     choice = input("do you want to draw another card, Y and N").lower()
#     if choice == "y":
#         del_card()
#         calculate_score(result)
#     else:
#         print("Game is over")
