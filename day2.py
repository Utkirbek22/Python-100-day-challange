# print("Number of lettters in your name: " + str(len(input("Enter your name"))))


print("Welcome to the tip calculator!")

bill = float(input("What was the bill ? $"))

tip = float(input("How much tip would you like to give ? 10, 12, or 15 ? $"))

people = float(input("How many people to split the bill ?  $" ))

result = round(bill * tip / people)

print(f"Each person has to pay: $ {result}")