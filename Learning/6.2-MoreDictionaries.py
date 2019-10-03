favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    # the last comma was placed there on purpose. getting ready to add in the future as a python best practice
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

# Now let's loop
print('\n"Let the looping begin biatches!!"')
for k, v in favorite_languages.items():  # k,v are abbreviation for Key and Value
    print(k.title() + "'s favorite language is " + v.title())

print('\n"Only grab the Keys"')
for name in favorite_languages.keys():  # can leave off .keys() here since that is the default if no method is passed
    print(name.title())

print('\n"Only grab the Keys - Methodless"')
for name in favorite_languages:
    print(name.title())

# List and Dictionary
print('\n"List and Dict"')
friends=['phil','sarah']
for name in favorite_languages.keys():
    # print(name.title())
    if name in friends:
        print("Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

# Not in list
print('\n"Not in Dictionary"')
if 'erin' not in favorite_languages.keys():
    print('Erin, please take the poll.')

# Looping through Keys in order
print('\n"Looping through Keys in order"')
for name in sorted(favorite_languages.keys()): # use SORTED
    print(name.title() + ", thank you for taking the poll.")

# Looping through Values
print('\n"Looping through Values"')
print("The following languages have been mentioned")
for language in favorite_languages.values():
    print(language.title())

# Looping through Values removing dupes
print('\n"Looping through Values removing dupes"')
print("The following languages have been mentioned")
for language in set(favorite_languages.values()):# use SET
    print(language.title())
