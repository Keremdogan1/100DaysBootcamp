def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(add=3, multiply=5)
class Car:
    def __init__(self, **kwargs):
        """ self.brand = kwargs["brand"]
        self.model = kwargs["model"] #Gives error if you dont enter these arguments """
        self.brand = kwargs.get("brand")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

car1 = Car(brand = "Bugatti", model = "Chiron")
car2 = Car(brand = "Bugatti")
print(car1.brand, car1.model)
print(car2.brand, car2.model)
