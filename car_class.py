from typing import Self


class Car:
    def __init__(
            self, year_of_issue: int, producer: str | int, mark: str
            , fuel_consumption: float, cost_of_service: int | float
    ):
        self.year_of_issue = year_of_issue
        self.producer = producer
        self.mark = mark
        self.mileage = 0
        self.fuel_consumption = fuel_consumption
        self.cost_of_service = cost_of_service

    def drive(self):
        return f"Я авто марки {self.mark}, їду по справам господаря"

    @property
    def category(self):
        if self.cost_of_service > 15000:
            return "Крутяк"
        else:
            return "Тачелла"


lamborghini = Car(year_of_issue=2023, mark="Lamborghini", producer="Italia", fuel_consumption=18.0,
                  cost_of_service=500000)
ferrari = Car(year_of_issue=2022, mark="Ferrari", producer="Italia", fuel_consumption=15.8, cost_of_service=700000)
rolls_royce = Car(year_of_issue=2023, mark="Rolls-Royce", producer="United Kingdom", fuel_consumption=14.5,
                  cost_of_service=600000)
ford = Car(year_of_issue=2018, mark="Ford", producer="USA", fuel_consumption=6.2, cost_of_service=12000)

ferrari.mileage = 5000

print(ford.category)

print(lamborghini.drive())
print(ferrari.mileage)
