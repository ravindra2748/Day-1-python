class Car:

    total_car = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
    
    def get_brand(self):
        return self.__brand 
    
    def set_brand(self,new_brand):
        self.__brand = new_brand

    def fullname(self):
        return (f"{self.__brand},{self.__model}")
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def general_info():
        return "Car have 4 wheels"
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self,battery_size,brand,model):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"
    


# my_electic_car = ElectricCar("4500","Toyota","fortuner")

# print(isinstance(my_electic_car,Car))
# print(isinstance(my_electic_car,ElectricCar))

# Car("TATA","Safari")
# my_car = Car("TATA","Nexon")
# my_car.model = "cait"
# print(my_car.model)
# print(Car.general_info())
# print(my_electic_car.fuel_type())
# print(safari.fuel_type())
# print(safari.fuel_type())
# print(Car.total_car)
# print(my_car.general_info())
# print(Car.general_info())

# print(my_electic_car.brand)
# print(my_electic_car.get_brand())
# my_electic_car.set_brand("BMW")
# print(my_electic_car.get_brand())
# print(my_electic_car.brand)

# my_car = Car("Toyota","Fortuner")
# print(my_car.brand,my_car.model)
# print(my_car.fullname())
# my_new_car = Car("Tata","Safari")
# print(my_new_car.model)
# my_electic_car.battery_size,my_electic_car.brand)
# print(my_electic_car.fullname())
# print(my_electic_car.model,

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCarTwo("tesla","Model s")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
