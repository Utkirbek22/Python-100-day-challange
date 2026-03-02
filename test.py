# numbers = 1_000
#
# for num in range(1, numbers):
#     total = 0
#     for i in range(1, num):
#         if num % i == 0:
#             total += i
#
#     if num == total:
#         print(num)
from urllib.parse import uses_relative

# 0 1 1 2 3 5 8 13 21 34 55

# numbers = 1000


# saved_contact = []
# saved_phone_number = []
#
# user = int(input("to choose saving the contact, press 1 and for numbers, press 2 or if you quite press 3: "))
# while user != 3:
#     if user == 1:
#         user_contact = input("enter the name you would like to save: ").lower()
#         if user_contact not in saved_contact:
#             saved_contact.append(user_contact)
#         else:
#             print(f"this user, {user_contact} is already saved")
#
#         user = int(input("to choose saving the contact, press 1 and for numbers, press 2: "))
#
#     elif user == 2:
#         user_numer = int(input("enter phone number: "))
#         if user_numer not in saved_phone_number:
#             saved_phone_number.append(user_numer)
#         else:
#             print(f"this number {user_numer} is already added")
#         user = int(input("to choose saving the contact, press 1 and for numbers, press 2: "))
#
# print(saved_contact)
# print(saved_phone_number)


person_info = {}
#
# user = int(input("""
# Please select the command:
# 1. Save
# 2. Search
# 3. Exit
# """))
#
# while user != 3:
#     if user == 1:
#         enter_name = input("Enter the name you would like to save: ").lower()
#         if enter_name not in person_info:
#             enter_number = int(input("enter phone number"))
#             person_info[enter_name] = enter_number
#         else:
#             print(f"here is {enter_name}: {person_info[enter_name]} info  ")
#         user = int(input("""
#         Please select the command:
#         1. Save
#         2. Search
#         3. Exit
#         """))
#
#
#     # print(person_info)
#
#     elif user == 2:
#         searched_name = (input("which name of person do you want to have ? ")).lower()
#         if searched_name not in person_info:
#             print(f"{searched_name} isn't in the saved contacts")
#         else:
#             print(f"this name {searched_name} {person_info[searched_name]} is already saved")
#         user = int(input("""
#         Please select the command:
#         1. Save
#         2. Search
#         3. Exit
#         """))
#
# print(person_info)

#  if AND entered, then the rest of 0 0 0 has to be printed each row and each col










user = int(input("enter number"))

for i in range(1,user + 1):
    print(i)













