# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# for student in student_scores:
#     print(student)


def find_highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bif of ${highest_bid}")

bids = {}
continue_bidding = True


while continue_bidding:
    name = input(" What is your name: ")
    price = int(input("How much you wanna invest: $"))
    bids[name] = price
    should_continue = input("Are you any other bidders ? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)


