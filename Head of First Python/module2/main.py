names = ["BMW", "Lambo", "Merc", "Audi","Ferrari", ["GT-7", "M5", [ "Utkirbek", "Jack", "Bonu", "Shahboz"]]]


def nested(go,indent = False,level=0):
    for each_item in go:
        if isinstance(each_item,list):
            nested(each_item,True, level + 1)
        else:
            if indent:
                for i in range(level):
                    print("\t", end='')
                print(each_item)

nested(names,True,-2)