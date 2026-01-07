import random



# total = 0
# for i in nums:
#     total += i
#
# print(total)
#
# max_num = 0
#
# for i in nums:
#     if i > max_num:
#         max_num = i
# print

#  Coding challange

letters = [
    "a","b","c","d","e","f","g","h","i","j",
    "k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z"
]

numbers = ["0","1","2","3","4","5","6","7","8","9"]

symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*",
    "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", "|",
    ";", ":", "'", '"', ",", ".", "<", ">", "?",
    "/", "\\", "~", "`"
]

print("Welcome to my password generator")

user_letters = int(input("How many letters would you like to have in your password ?: \n "))
user_symbols = int(input("How many symbols do you wanna have ? \n" ))
user_nums = int(input("How many numbers would you like to have ?:\n "))
#
# password = ""
# for i in range(1, user_letters + 1):
#     password += random.choice(letters)
# for _ in range(1, user_symbols + 1):
#     password += random.choice(symbols)
# for _ in range(1, user_nums + 1):
#     password += random.choice(numbers)
#
# print(password)

my_password = []


for _ in range(0, user_letters):
    my_password.append(random.choice(letters))

for _ in range(0, user_symbols):
    my_password.append(random.choice(symbols))

for _ in range(0, user_nums):
    my_password.append(random.choice(numbers))

print(my_password)
random.shuffle(my_password)
print(my_password)

password = ""

for char in my_password:
    password += char

print(f"Your password is {password}")














