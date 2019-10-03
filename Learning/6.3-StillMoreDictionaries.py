# Creating a List of Dictionaries
print('\n"Creating a List of Dictionaries"')
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

aliens1=[alien_0,alien_1,alien_2]

for alien1 in aliens1:
    print(alien1)

# Create a fleet of aliens
print('\n"Create a fleet of aliens"')

aliens2=[] # Make an empty list

for alien_number2 in range(30): # Make 30 new aliens
    new_alien2 = {'color':'green','points':5,'speed':'slow'}
    aliens2.append(new_alien2)

for alien2 in aliens2[:5]: # Show the first 5 aliens
    print(alien2)
print("...")

print("Total number of aliens: " + str(len(aliens2))) # Show how may aliens have been created

# Change some aliens
print('\n"Change some aliens"')

aliens3=[] # Make an empty list

for alien_number3 in range(30): # Make 30 new aliens
    new_alien3 = {'color':'green','points':5,'speed':'slow'}
    aliens3.append(new_alien3)

for alien3 in aliens3[0:3]: # Change the first 3 aliens
    if alien3['color']=='green':
        alien3['color']='yellow'
        alien3['speed']='medium'
        alien3['points']=10

for alien3 in aliens3[:5]: # Show the first 5 aliens
    print(alien3)
print("...")

# Use List in a Dictionary
print('\n"Use List in a Dictionary"')
pizza={
    'crust':'thick',
    'toppings': ['mushrooms','extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# favorite_languages 2.0
print('\n"favorite_languages 2.0"')
favorite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
for name, languages in favorite_languages.items():
    if len(languages)< 2:
        for language in languages:
            print("\n" + name.title() + "'s favorite languages is " + language.title())


# Using a Dictionary in a Dictionary
print('\n"Using a Dictionary in a Dictionary"')
users = {
    'aeinstein': {
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie': {
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLoation: " + location.title())