import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260403.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrel_count)
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrel_count)
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrel_count)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count,red_squirrel_count,black_squirrel_count]
}


intfo = pandas.DataFrame(data_dict)
print(intfo)