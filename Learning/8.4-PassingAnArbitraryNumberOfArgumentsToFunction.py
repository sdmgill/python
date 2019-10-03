# the wildcard * makes Python throw everything into a tuple even if a single argument is passed.
def make_pizza(*toppings):
    """Print the list of toppings"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('pepperoni','sausage','onions')

# same thing but loop through
def make_pizza(*toppings):
    """Print the list of toppings"""
    print("\nMaking pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('pepperoni','sausage','onions')

# mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are going to make"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16,'pepperoni')
make_pizza(16,'pepperoni','sausage','onions')

# using arbitrary keyword arguments - a ** causes Python to create an empty dictionary
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    profile={}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',
                             location='princeton',
                             field = 'physics')
print(user_profile)