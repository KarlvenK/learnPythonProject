<<<<<<< HEAD
# superclass
class Car:

=======
#superclass
class Car():
    
>>>>>>> origin/master
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
<<<<<<< HEAD

    def read_odometer(self):
        print("this cat has " + str(self.odometer_reading) + "miles on it")

=======
    
    def read_odmeter(self):
        print("this cat has " + str(self.odometer_reading + "miles on it"))
    
>>>>>>> origin/master
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can not roll back an odometer")
<<<<<<< HEAD

=======
    
>>>>>>> origin/master
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        self.gas_tank = 100


<<<<<<< HEAD
# subclass
# inherited from Car
class ElectricCar(Car):
    """电动车的独特之处"""

=======
#subclass
#inherited from Car    
class ElectricCar(Car):
    """电动车的独特之处"""
>>>>>>> origin/master
    def __init__(self, make, model, year):
        """initialize the property from super class"""
        super().__init__(make, model, year)
        self.battery = Battery()
<<<<<<< HEAD

    """override the func of superclass"""

=======
    
    """overred the func of superclass"""
>>>>>>> origin/master
    def fill_gas_tank(self):
        print("this car doesn't have a gas tank!")


<<<<<<< HEAD
class Battery:
    def __init__(self, battery_size=70):
=======
class Battery():
    def __init__(self, battery_size = 70):
>>>>>>> origin/master
        self.battery_size = battery_size

    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "-kWh battery")
<<<<<<< HEAD
=======
    
>>>>>>> origin/master


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
