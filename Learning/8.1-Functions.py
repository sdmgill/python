# simple function
def greet_usr():
    """Display a simple greeting"""
    print("Hello")

greet_usr()

# passing a variable to a function
def greet_user(username):
    """Display a simple greeting"""
    print("Hello " + username.title() + "!")

greet_user('sean')

# postional arguments
def describe_pet(animal_type,pet_name):
    """Display info about a pet"""
    print("\nI have a " + animal_type +".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

    """You can call a function multiple times after it has been defined"""
describe_pet('cat','buddy')
describe_pet('dog','peanut')

# keyword arguments
def describe_pet(animal_type,pet_name):
    """Display info about a pet"""
    print("\nI have a " + animal_type +".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

    """once you pass a keyword argument, you have to use all the keywords in the function or the call will fail. For example, you cannot pass (animal_type = 'cat','buddy)
        the exceptio is if you have a default defined as in the next section"""
describe_pet(animal_type='frog',pet_name='ribbit')
describe_pet(animal_type='lizard',pet_name='geico')

# default values - defaults need to be listed after parameters without defaults.
def describe_pet(pet_name,animal_type = 'dog'):
    """Display info about a pet"""
    print("\nI have a " + animal_type +".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='killer')
describe_pet('tom')

# you can override defaults
def describe_pet(pet_name,animal_type = 'dog'):
    """Display info about a pet"""
    print("\nI have a " + animal_type +".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

    """When using keywords, the order is not important. I reversed the order below on purpose"""
describe_pet(animal_type='hampster',pet_name='harry')
