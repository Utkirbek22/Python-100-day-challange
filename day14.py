import random
import day14data

# a = random.choice(day14data.data)
# b = random.choice(day14data.data)
# if a == b:
#     b = random.choice(day14data.data)
# count = 0
# print(f"Compare A: {a["name"]}, {a["follower_count"]}, {a["description"]}, {a["country"]}")
# print(f"compare B: {b["name"]}, {b["follower_count"]}, {b["description"]}, {b["country"]}")
# user = input("enter the A or B").lower()
#
# if user == "a" and a["follower_count"] > b["follower_count"]:
#     print(f"a {a["follower_count"]} is higher than b {b["follower_count"]} ")
#     count += 1
# else:
#     print("sorry, that is wrong")
#
#
# if user == "b" and b["follower_count"] > a["follower_count"]:
#     print(f"a {b["follower_count"]} is higher than b {a["follower_count"]} ")
#     count += 1
# else:
#     print("that one is also wrong")



# or user == "b" and b["follower_count"] > a["follower_count"]:

 #
 # if a["follower_count"] == b["follower_count"]:
 #        print("it is draw")

# def format_data(account):
#     account_name = account["name"]
#     account_followers = account["follower_count"]
#     account_desc = account["description"]
#     account_country = account["country"]
#     # return account_name, account_followers, account_desc, account_country
#     return f"{account_name}, {account_followers}, {account_desc}, {account_country}"
#
# def check_answer(user_guess,a_follower,b_follower):
#     if a_follower > b_follower:
#         return  user_guess == "a"
#     else:
#         return  user_guess == "b"
# count = 0
#
# game_should_continue = True
# #  generate a random account from game data
# b = random.choice(day14data.data)
#

#
# while game_should_continue:
#     a = b
#     b = random.choice(day14data.data)
#     if a == b:
#         b = random.choice(day14data.data)
#     #  format the account data into printable format
#     print(f"Compare A {format_data(a)} \n")
#     print(f"Against B {format_data(b)} \n")
#     # Ask user for a guess
#     user = input("who has more followers, Type A or B").lower()
#
#     # Check if user is correct
#     # Get follower count for each account
#     a_follower_account = a["follower_count"]
#     b_follower_account = b["follower_count"]
#     is_correct = check_answer(user,a_follower_account, b_follower_account)

    #  Use if statament to check if user is correct
    # if a_follower_account > b_follower_account:
    #     if user == "a":
    #         print(f"you are right, you current score {count}")
    #         count += 1
    #     else:
    #         print(f"ohh, that is wrong, your final score is {count}")
    # else:
    #     print(f"ohh, that is wrong, your final score is {count}")

    # Give user feedback on their guess
    #
    # if is_correct:
    #     count += 1
    #     print(f"you are right, current score is {count} \n")
    # else:
    #     print(f"ohh sorry, that is wrong, you final score is {count}")
    #     game_should_continue = False
    # #  score keeping

    # Make the game repeatable

def format_data(account):
    account_name = account["name"]
    account_followers = account["follower_count"]
    account_desc = account["description"]
    account_country = account["country"]
    # return account_name, account_followers, account_desc, account_country
    return f"{account_name}, {account_followers}, {account_desc}, {account_country}"

def check_answer(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"


count = 0

game_should_continue = True
    #  generate a random account from game data
b = random.choice(day14data.data)

while game_should_continue:
    a = b
    b = random.choice(day14data.data)
    if a == b:
        b = random.choice(day14data.data)

    print(f"Compare A {format_data(a)} \n")
    print(f"Against B {format_data(b)} \n")

    user = input("who has more followers, Type A or B").lower()


    a_follower_account = a["follower_count"]
    b_follower_account = b["follower_count"]
    is_correct = check_answer(user,a_follower_account, b_follower_account)


    if is_correct:
        count += 1
        print(f"you are right, current score is {count} \n")
    else:
        print(f"ohh sorry, that is wrong, you final score is {count}")
        game_should_continue = False
