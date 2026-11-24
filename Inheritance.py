class vehicle ():

    def __init__(self,brand ,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start (self):
        print("It started ")

    def stop (self):
        print("it stopped")


class car(vehicle):

    def __init__(self, brand, model, year,no_of_doors,mileage):
        super().__init__(brand, model, year)
        self.no_of_doors = no_of_doors
        self.mileage = mileage


class bike(vehicle):

    def __init__(self, brand, model, year,gears):
        super().__init__(brand, model, year)
        self.gears = gears



Car = car("Toyota","acura","2020","4","50")
Bike = bike("honda","def","2018","6")

print(Car.__dict__)
