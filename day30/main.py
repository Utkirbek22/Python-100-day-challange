# with open("data.txt") as data_file:
#     data_file.read()

# try:
#     file1 = open("data.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     # print("there is an error")
#     file1 = open("data.txt","w")
#     file1.write("anything I want")
# except KeyError as err_mess:
#     print(f"The key is {err_mess} does not exist.")
# else:
#     content = file1.read()
#     print(content)
# finally:
#     raise TypeError("That is error that i made up")










try:
    file = open("data.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("data.txt", "w")
    file.write("All i want is to make my family happy")

except KeyError as err_mess:
    print(f"the key {err_mess} does not exist")
else:
    content = file.read()
    print(content)










