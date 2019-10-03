# 6-1
print('"6-1"')
friend = {
    'first_name': 'dinna',
    'last_name': 'gill',
    'age': '52',
    'city': 'phoenix',
}

print("My best friend's name is " + friend['first_name'].title() + " " +
      friend['last_name'].title() + '. She is ' + str(friend['age']) +
      ' years old and lives in ' + friend['city'].title() + ".")

# 6-2
print('\n"6-2"')
favorite_numbers = {
    'dinna': 52,
    'connor': 19,
    'bulldog': 17,
    'buddy': 7,
    'debrickashaw': 51,
}
print("Dinna's favorite number is " + str(favorite_numbers['dinna']) + ".")
print("Connor's favorite number is " + str(favorite_numbers['connor']) + ".")
print("Bulldog's favorite number is " + str(favorite_numbers['bulldog']) + ".")
print("Buddy's favorite number is " + str(favorite_numbers['buddy']) + ".")
print("Debrickashaw's favorite number is " + str(favorite_numbers['debrickashaw']) + ".")

# 6-3
print('\n"6-3"')
word_list = {
    'dictionary': 'A piece of data or values that can be accessed by a key(word) you have at hand.',
    'glossary': 'Similar to dictionary but think of it as a dictionary to store a dictionary',
    'butt-nugget': 'Nothing to do with Python at all',
    'Cheeseburger': 'What I want for lunch.',
    'PyCharm': 'New Python IDE I purchased.',
}
for key, value in word_list.items():
    print("\nWord: " + key)
    print("Definition: " + value)

# 6-4 Already did for 6-3 solution
# 6-5 Did enough if this in 6.2-MoreDictionaries.py

# 6-6
print('\n"6-6"')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    # the last comma was placed there on purpose. getting ready to add in the future as a python best practice
}

class_list =['tony','jen','barb','sarah','tom','edward','phil','debrickashaw']
for student in class_list:
    if student not in favorite_languages.keys():
        print(student.title() + ", please take the poll.")
for student in class_list:
    if student in favorite_languages.keys():
            print(student.title() + ", thank you for taking the poll.")
# for name in favorite_languages.keys():
#     if name in class_list:
#         print(name.title() + ", thank you for taking the poll.")

# 6-7
print('\n"6-7"')
wife = {
    'first_name': 'dinna',
    'last_name': 'gill',
    'age': '52',
    'city': 'phoenix',
    'relationship': 'wife',
    'gender': 'f',
}

oson = {
    'first_name': 'connor',
    'last_name': 'gill',
    'age': '19',
    'city': 'tuscaloosa',
    'relationship': 'oldest son',
    'gender': 'm',
}

yson = {
    'first_name': 'bulldog',
    'last_name': 'gill',
    'age': '18',
    'city': 'glendale',
    'relationship': 'youngest son',
    'gender': 'm',
}

family = [wife,oson,yson]
for member in family:
    if member['gender'] == 'm':
        print(member['first_name'].title() + " is my " + member['relationship'] + ". He is " + member['age'] + " years old and lives in " + member['city'].title() + ".")
    if member['gender'] == 'f':
        print(member['first_name'].title() + " is my " + member['relationship'] + ". She is " + member['age'] + " years old and lives in " + member['city'].title() + ".")

# 6-8 same as 6-7

# 6-9
favorite_places = {
    'dinna':['phillipines','london','spain'],
    'Sean':['hawaii','phoenix'],
    'buddy':['litter box','floor muffin']
}

for name,places in favorite_places.items():
    print("\n"+ name.title()+ "'s favorite places are:")
    for place in places:
        print(place.title())

# 6-10
cities = {
    'phoenix':{
        'temperature':'hot',
        'humidity':'low',
        'population':'1,600,000',

    },
    'tuscaloosa':{
        'temperature':'medium',
        'humidity':'medium',
        'population':'99,543',
    }
}

for city_name,city_info in cities.items():
    print("\nHere are some interesting facts about " + city_name.title())
    print('Temperature is '+ city_info['temperature'].title())
    print('Humidity is ' + city_info['humidity'].title())
    print('Population is ' + city_info['population'].title())

