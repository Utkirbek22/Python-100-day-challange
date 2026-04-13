def add(*args):
    print(2,3,4,5,6)

add()

def row(*args):
    for i in args:
        print(i)

row(1,2,3,4)


def nums(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

result = nums(3,4,7,8,2)
print(result)


#  kwargs arguments

def calculate(n,**kwargs):
    print(n,kwargs)
    n += kwargs["add"]
    n *= kwargs["multi"]
    print(n)
calculate(2, add=3, multi=8)


def second_calc(n ,*args):
    print(args)
    for i in args:
        n += i
        n *= i
        n -= i
    print(n)
second_calc(2,5,5,1)



class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("make")
        self.year = kwargs.get("year")


my_new_car = Car(make="Nissan", year=22)

print(my_new_car.make,"\n", my_new_car.year)






