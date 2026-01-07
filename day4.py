import random

# num = random.uniform(1, 10)
#
#
#
# if num < 5:
#     print("Heads")
# else:
#     print("tails")

#
# names = ["Jack", "Utkirbek", "Bonu", "Shaxboz"]
#
# choose = random.choice(names)
#
# random_index = random.randint(0,4)
#
# print(choose)
#
# print(names[random_index])


choice = ["rock", "scissors",  "paper"]
me = input('Choose one of the options, "rock", "Scissors",  "paper"').lower()

computer = random.choice(choice)

print(f"You chose: {me}")
print(f"Computer chose: {computer}")

if me == computer:
    print("it is draw")
elif ((me == "rock" and computer == "scissors") or
      (me == "scissors" and computer == "paper") or
      (me == "papper" and computer == "rock")
):
    print("🎉 You win!")
else:
    print("You lost !")



