# my_car.py
from car import Car

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# my_electric_car.py
from car import ElectricCar

my_tesla = ElectricCar('tesla','model s', 2016)
print("\n" + my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# my_cars.py
from car import Car, ElectricCar

my_beetle = Car('volkswagon','beetle', 2016)
print("\n" + my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','model s', 2017)
print(my_tesla.get_descriptive_name())

# my_cars.py version 2 -- import the entire Class
import car

my_beetle = Car('volkswagon','beetle', 2017)
print("\n" + my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','model s', 2018)
print(my_tesla.get_descriptive_name())