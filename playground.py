# it is possible to have an unlimited number of arguments passed into a function
def add(*args):
    # print(args[0])

    sum = 0
    for arg in args:
        sum += arg
        # print(arg)

    print(f"sum: {sum}")
    return sum

add(3,5,6,2,5,8,0,4,6)

# it is possible to have unlimited keyword arguments
def calculate(n, **kwargs):
    # print(type(kwargs))
    # print(kwargs)
    # print(kwargs["add"])
    # print(kwargs["multiply"])

    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(f"n: {n}")

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.seats = kw.get("seats")
        """with declarations like this, if the value doesnt exist when initiated, it will fail
        However if we use the dictionary ".get" like we do above, then it doesnt fail"""
        # self.make = kw["make"]
        # self.model = kw["model"]

my_car = Car(make="Nissan", model="Skyline", seats=4)
print(my_car.make)
print(my_car.model)
print(my_car.seats)