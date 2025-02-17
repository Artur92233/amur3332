from abc import abstractmethod, ABC


class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Транспортний засіб: {self.brand}  {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    @abstractmethod
    def info(self):
        print(f"Автомобіль: {self.brand} {self.model}, Кількість дверей: {self.num_doors}")


class Bike(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type

    def info(self):
        print(f"Велосипед: {self.brand} {self.model}, Тип: {self.type}")


class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def info(self):
        print(f"Вантажівка: {self.brand} {self.model}, Вантажопідйомність: {self.capacity} тонн")


car1 = Car(brand="Toyota", model="Corolla", num_doors=4)
car2 = Car(brand="BMW", model="X5", num_doors=4)

bike1 = Bike(brand="Giant", model="Escape 3", type="міський")
bike2 = Bike(brand="Trek", model="Marlin 8", type="гірський")

truck1 = Truck(brand="Volvo", model="FH16", capacity=20)
truck2 = Truck(brand="Scania", model="R500", capacity=25)

car1.info()
car2.info()
bike1.info()
bike2.info()
truck1.info()
truck2.info()
