class Car:
    def __init__(self, maker, model, color, price):
        self.maker = maker
        self.model = model
        self.color = color
        self.price = price

    def setMaker(self, maker):
        self.maker = maker

    def getMaker(self):
        return self.maker

    def __str__(self):
        return f"maker: {self.maker}, model: {self.model}, color: {self.color}, price: {self.price}"

    def getDesc(self):
        return self.__str__()
    
class ElectricCar(Car):
    def __init__(self, maker, model, color, price, bat_size):
        super().__init__(maker, model, color, price)
        self.bat_size = bat_size

    def set_bat_size(self, bat_size):
        self.bat_size = bat_size

    def get_bat_size(self): 
        return self.bat_size

    def __str__(self):
        return f"{super().__str__()}, Battery : {self.bat_size}"

    def getDesc(self):
        return self.__str__()

class Truck(Car):
    def __init__(self, maker, model, color, price, payLoad):
        super().__init__(maker, model, color, price)
        self.payLoad = payLoad

    def set_payLoad(self, payLoad):
            self.payLoad = payLoad
    
    def get_payLoad(self): 
            return self.payLoad
    
    def __str__(self):
            return f"{super().__str__()}, PayLoad : {self.payLoad}"
    
    def getDesc(self):
            return self.__str__()


def main():

    car1 = ElectricCar("Tisla", "Model S", "white", 100000, 0)
    car1.setMaker("Tesla")
    car1.set_bat_size(60)
    print(car1.getDesc())

    car2 = Truck("Kia", "truw", "Blue", 120000, 5000)
    car2.setMaker("Cclass")
    car2.set_payLoad(6000)
    print(car2.getDesc())

    print(type(car1))
    print(type(car2))

    print(isinstance(car1, ElectricCar))
    print(isinstance(car2, Truck))
    print(isinstance(car1, Car))
    print(isinstance(car2, Car))


main()