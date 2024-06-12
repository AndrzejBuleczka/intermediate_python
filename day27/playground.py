def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(2, 3, 10))


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="Micra")
print(my_car.make)
