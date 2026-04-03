# with open("weather_data.csv", mode="r") as data:
#     weather_future = data.readlines()
#     print(weather_future)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     tempratures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)
#
#


import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data["temp"]))


data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

# avr = 0
# for num in temp_list:
#     avr += num
# average = avr / len(temp_list)
# print(average)


# max = 0
#
# for num in temp_list:
#     if num > max:
#         max = num
#
# print(max)

print(data["temp"].mean())
print(data["temp"].max())

# Get data in Columns

print(data["condition"])
print(data.condition)

# Get Data in Row

print(data[data.day == "Monday"])

print(data[data.day == 24])

print(data[data.temp == data.temp.max()])













