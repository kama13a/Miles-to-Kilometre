# *args -- unlimited arguments
# python treats the *args as tuple
# the *args also called "Unlimited Positional Arguments"
def add(*args):
    print(args[0])  # You can tap in like this
    summ = 0
    for n in args:
        summ += n
    print(summ)


add(1,23,45,566,77,5)


class Car:
    def __init__(self, **kwargs):
        self.model = kwargs.get("model")
        self.color = kwargs["color"]

my_car = Car(model=100, color="red")
print(my_car.model)