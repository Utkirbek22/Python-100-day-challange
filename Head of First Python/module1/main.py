# names = ["BMW", "Lambo", "Merc", "Audi","Ferrari"]
#
# print(names)
#
# print(len(names))
# print(names[0])
#
# names.pop()
# print(names)
#
# names.append("Toyoto")
# print(names)
#
# names.extend("Volvagan")
# print(names)
#
# names.remove("Lambo")
# print(names)
# names.insert(0,"Lambo")
# print(names)




#  Lists withins Lists


names = ["BMW", "Lambo", "Merc", "Audi","Ferrari", ["GT-7", "M5", [ "Utkirbek", "Jack", "Bonu", "Shahboz"]]]
# print(names)

# for name in names:
    # if isinstance(name,list):
    #     for nested_name in name:
    #         if isinstance(nested_name,list):
    #             for deeper_nested in nested_name:
    #                 print(deeper_nested)
    #         else:
    #             print(nested_name)
    # else:
    #     print(name)




# Recursion

# def lol(the_list):
#     for item in the_list:
#         if isinstance(item,list):
#             lol(item)
#         else:
#             print(item)
#
# lol(names)