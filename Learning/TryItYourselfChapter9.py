# 9-1
class Restaurant():
    """Class for a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Define init method"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant"""
        print("The restaurant " + self.restaurant_name.title() + " serves " + self.cuisine_type.title() + " style food.")

    def open_restaurant(self):
        """Is the restaurant open"""
        print(self.restaurant_name.title() + " is now open for business.")

restaurant = Restaurant('fogo de chao','brazillian')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2 just adding additional instances to to 9-1
print("\n")
restaurant2 = Restaurant('5 guys','burger especial')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

print("\n")
restaurant3 = Restaurant('midos','japanese')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

# 9-3
class User():
    """Creating a simple class to track user attributes"""

    def __init__(self, f_name, l_name, age, city, state):
        """Initialize attributes"""
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.city = city
        self.state = state

    def describe_user(self):
        """method for describing user attributes"""
        print("The user " + self.f_name.title() + " " + self.l_name.title() + " is " + str(
            self.age) + " years old and lives in " +
              self.city.title() + ", " + self.state.title() + ".")

    def greet_user(self):
        """Method for greeting the user"""
        print("Greetings " + self.f_name.title() + " " + self.l_name.title() + " we hope you enjoy your stay with us!")


user1 = User('sean', 'gill', '47', 'phoenix', 'arizona')
user1.describe_user()
user1.greet_user()

print("\n")
user2 = User('dinna', 'gill', '52', 'phoenix', 'arizona')
user2.describe_user()
user2.greet_user()

print("\n")
user3 = User('bulldog', 'gill', '18', 'glendale', 'arizona')
user3.describe_user()
user3.greet_user()

# 9-4
class Restaurant():
    """Class for a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Define init method"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print("The restaurant " + self.restaurant_name.title() + " serves " + self.cuisine_type.title() + " style food.")

    def open_restaurant(self):
        """Is the restaurant open"""
        print(self.restaurant_name.title() + " is now open for business.")

    def read_number_served(self):
        """See how many customers we have served"""
        print("We have served " + str(self.number_served) + " patrons.")

    def set_number_served(self, served):
        """Update the number of customers served"""
        self.number_served = served

    def increment_number_served(self, added):
        """Adds a value to the number of customers served"""
        self.number_served += added


restaurant = Restaurant('fogo de chao','brazillian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(25)
restaurant.read_number_served()
restaurant.increment_number_served(20)
restaurant.read_number_served()

# 9-5
class User():
    """Creating a simple class to track user attributes"""

    def __init__(self, f_name, l_name, age, city, state):
        """Initialize attributes"""
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.city = city
        self.state = state
        self.login_attempts = 0

    def describe_user(self):
        """method for describing user attributes"""
        print("The user " + self.f_name.title() + " " + self.l_name.title() + " is " + str(
            self.age) + " years old and lives in " +
              self.city.title() + ", " + self.state.title() + ".")

    def greet_user(self):
        """Method for greeting the user"""
        print("Greetings " + self.f_name.title() + " " + self.l_name.title() + " we hope you enjoy your stay with us!")

    def read_login_attempts(self):
        """Method to read the number of login attempts"""
        print("Current login attempts: " + str(self.login_attempts) + ".")

    def increment_login_attempts(self):
        """Increments login attemps by 1"""
        self.login_attempts = self.login_attempts + 1

    def reset_login_attemts(self):
        """Reset the user's login attemtps to 0"""
        self.login_attempts = 0


user1 = User('sean', 'gill', '47', 'phoenix', 'arizona')
user1.describe_user()
user1.greet_user()
user1.read_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.read_login_attempts()
user1.reset_login_attemts()
user1.read_login_attempts()
user1.increment_login_attempts()
user1.read_login_attempts()

# 9-6
class Restaurant():
    """Class for a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Define init method"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(
            "The restaurant " + self.restaurant_name.title() + " serves " + self.cuisine_type.title() + " style food.")

    def open_restaurant(self):
        """Is the restaurant open"""
        print(self.restaurant_name.title() + " is now open for business.")

    def read_number_served(self):
        """See how many customers we have served"""
        print("We have served " + str(self.number_served) + " patrons.")

    def set_number_served(self, served):
        """Update the number of customers served"""
        self.number_served = served

    def increment_number_served(self, added):
        """Adds a value to the number of customers served"""
        self.number_served += added


class IceCreamStand(Restaurant):
    """A special type of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the attributes of the Parent Class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def get_flavors(self):
        """
        Print the list of flavors we have
        I needed to research the "strip" portion online. Not sure if the book really wanted a LIST for flavors
        """
        print("We serve: " + (str(self.flavors).strip('[]') + "."))


dessert = IceCreamStand('Cold Stone', 'Ice Cream')
dessert.describe_restaurant()
dessert.get_flavors()

# 9-7
class User():
    """Creating a simple class to track user attributes"""

    def __init__(self, f_name, l_name, age, city, state):
        """Initialize attributes"""
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.city = city
        self.state = state
        self.login_attempts = 0

    def describe_user(self):
        """method for describing user attributes"""
        print("The user " + self.f_name.title() + " " + self.l_name.title() + " is " + str(
            self.age) + " years old and lives in " +
              self.city.title() + ", " + self.state.title() + ".")

    def greet_user(self):
        """Method for greeting the user"""
        print("Greetings " + self.f_name.title() + " " + self.l_name.title() + " we hope you enjoy your stay with us!")

    def read_login_attempts(self):
        """Method to read the number of login attempts"""
        print("Current login attempts: " + str(self.login_attempts) + ".")

    def increment_login_attempts(self):
        """Increments login attemps by 1"""
        self.login_attempts = self.login_attempts + 1

    def reset_login_attemts(self):
        """Reset the user's login attemtps to 0"""
        self.login_attempts = 0

class Admin(User):
    """Define attributes for Admin users"""
    def __init__(self,f_name, l_name, age, city, state):
        """Initialize attributes from Parent Class"""
        super().__init__(f_name, l_name, age, city, state)
        self.privelages = ['can add post', 'can delete post', 'can ban user']

    def show_privelages(self):
        """Print the list of privelages"""
        print("Admin users can: " + (str(self.privelages).strip('[]') + "."))

LocalAdmin = Admin('sean','gill','47','phoenix','arizona')
LocalAdmin.describe_user()
LocalAdmin.show_privelages()

# 9-8
class User():
    """Creating a simple class to track user attributes"""

    def __init__(self, f_name, l_name, age, city, state):
        """Initialize attributes"""
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.city = city
        self.state = state
        self.login_attempts = 0

    def describe_user(self):
        """method for describing user attributes"""
        print("The user " + self.f_name.title() + " " + self.l_name.title() + " is " + str(
            self.age) + " years old and lives in " +
              self.city.title() + ", " + self.state.title() + ".")

    def greet_user(self):
        """Method for greeting the user"""
        print("Greetings " + self.f_name.title() + " " + self.l_name.title() + " we hope you enjoy your stay with us!")

    def read_login_attempts(self):
        """Method to read the number of login attempts"""
        print("Current login attempts: " + str(self.login_attempts) + ".")

    def increment_login_attempts(self):
        """Increments login attemps by 1"""
        self.login_attempts = self.login_attempts + 1

    def reset_login_attemts(self):
        """Reset the user's login attemtps to 0"""
        self.login_attempts = 0


class Privelages():
    """Simple method to describe Privelages"""

    def __init__(self, privelages=['can add post', 'can delete post', 'can ban user']):
        self.privelages = privelages

    def show_privelages(self):
        """Print the list of privelages"""
        print("Admin users can: " + (str(self.privelages).strip('[]') + "."))


class Admin(User):
    """Define attributes for Admin users"""

    def __init__(self, f_name, l_name, age, city, state):
        """Initialize attributes from Parent Class"""
        super().__init__(f_name, l_name, age, city, state)
        self.privelages = Privelages()


LocalAdmin = Admin('sean', 'gill', '47', 'phoenix', 'arizona')
LocalAdmin.describe_user()
LocalAdmin.privelages.show_privelages()

# 9-9
class Car():
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted desciptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll the odometer back!")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading.
        Also add logic to prevent a rollback
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll the odometer back!")


class Battery():
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement regarding the battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print statement about the range this battery size provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Method to upgrade the battery if battery is at the default value"""
        if self.battery_size ==70:
            self.battery_size = 85
            print("Battery upgraded!")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the Parect Class"""
        super().__init__(make, model, year)
        self.battery = Battery()  # create a new instance of the Battery Class here

my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()  # need to fully qualify the call to describe_battery now
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()  # need to fully qualify the call to describe_battery now
my_tesla.battery.get_range()

# 9-10 - 9-12 Review ClassesImporting for review

# 9-13
print('\n"Rewrite of 6-3 using OrderedDict()"')
from collections import OrderedDict

word_list = OrderedDict()

word_list['dictionary'] = 'A piece of data or values that can be accessed by a key(word) you have at hand.'
word_list['glossary'] = 'Similar to dictionary but think of it as a dictionary to store a dictionary'
word_list['butt-nugget'] = 'Nothing to do with Python at all'
word_list['Cheeseburger'] = 'What I want for lunch.'
word_list['PyCharm'] = 'New Python IDE I purchased.'

for key, value in word_list.items():
    print("\nWord: " + key)
    print("Definition: " + value)

# 9-14
from random import randint

class Die():
    def __init__(self, sides = 6):
        """Rolling some dice here"""
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)

    def update_die_sides(self,numsides):
        """Set the number of sided the dies has"""
        self.sides = numsides

rd = Die()
rd.update_die_sides(20)
rd.roll_die()

