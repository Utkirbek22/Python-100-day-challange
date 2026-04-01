# file = open("my_file.txt")
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
    # file.close()

with open("my_file.txt", mode="a") as file:
    file.write("don't give up, Man, everything will be great, just cut the distractions")


with open("new_file.txt", mode="a") as file:
    file.write("hello, Jack, are you ready to prepare for the exam")