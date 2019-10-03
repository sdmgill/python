# 8.1
def display_message():
    """Just adding a comment"""
    print("I am learning Functions in Chapter 8!")


display_message()


# 8.2
def favorite_book(title):
    """Yep"""
    print("One of my favorite books is " + title.title() + "!")


favorite_book('it')


# 8.3
def make_shirt(size, message):
    """Display shirt size and message"""
    print("\nYou ordered a " + size.title() + " shirt with the message '" + message.title() + "' printed on the front.")


make_shirt('l', 'fuck off')


# 8.4
def make_shirt(size='l', message='I Love Python'):
    """Display shirt size and message"""
    print("\nYou ordered a " + size.upper() + " shirt with the message '" + message.title() + "' printed on the front.")


make_shirt()
make_shirt('xl', 'fuck off')


# 8-5
def describe_city(city, country='United States'):
    """Describe a city and it's country"""
    print("\nThe city " + city.title() + " is located in " + country.title() + ".")


describe_city('toronto', 'canada')
describe_city('phoenix')
describe_city('davoe', 'phillipines')


# 8-6
def city_country(city, country):
    """Neatly return a city, country combo"""
    formatted_cc = city.title() + ', ' + country.title()
    return formatted_cc


place = city_country('toronto', 'canada')
print(place)

place = city_country('tempe', 'united states')
print(place)

place = city_country('mexico city', 'mexico')
print(place)


# 8-7
def make_album(artist_name, album_title, num_tracks=''):
    """Formatting album information in a dictionary"""
    album_dic = {'Artist Name': artist_name.title(), 'Album Title': album_title.title()}

    if num_tracks:
        album_dic['Number of Tracks'] = num_tracks

    return album_dic


album = make_album('the doors', 'this is the end')
print(album)

album = make_album('motley crue', 'wild side', 12)
print(album)


# 8-8
def make_album2(artist_name, album_title):
    """Formatting album information in a dictionary"""
    album_dic2 = {'Artist Name': artist_name.title(), 'Album Title': album_title.title()}

    return album_dic2


while True:
    print("\nList your favorite Album information: ")
    print("(Type 'q' at any time to exit)")

    art_name = input("Artist Name: ")
    if art_name == 'q':
        break

    al_title = input("Album Title: ")
    if al_title == 'q':
        break

    formatted_album = make_album(art_name, al_title)
    print(formatted_album)


# 8-9
def show_magicians(name):
    """Print the list of magician names"""
    for magician in name:
        print("Introducing " + magician.title() + "!")


magic_men = ['tony', 'fred', 'billy']
show_magicians(magic_men)


# 8-10
def make_great(old_name, new_name):
    while old_name:
        upgraded_name = old_name.pop()

        new_name.append(upgraded_name + " the Great")


def show_magicians(new_name):
    """Print the list of magician names"""
    for magician in new_name:
        print("Introducing " + magician.title() + "!")


old_name = ['tony', 'fred', 'billy']
new_name = []

make_great(old_name, new_name)
show_magicians(new_name)
show_magicians(old_name)  # nothing here since we modified the original list


# 8-11 Same as 8-10 but using a copy instead of modifying the original list
def make_great(old_name, new_name):
    while old_name:
        upgraded_name = old_name.pop()

        new_name.append(upgraded_name + " the Great")


def show_magicians(new_name):
    """Print the list of magician names"""
    for magician in new_name:
        print("Introducing " + magician.title() + "!")


old_name = ['tony', 'fred', 'billy']
new_name = []

make_great(old_name[:], new_name)
show_magicians(new_name)
show_magicians(old_name)  # something here since we used a copy this time around.

# 8-12
def make_sandwich(*ingred):
    print("\nMaking your sandwich with the following ingredients:")
    for item in ingred:
        print("-" + item)

make_sandwich('turkey')
make_sandwich('turkey','ham','roast beef')
make_sandwich('tomato','lettuce','onion','mayo')

# 8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    profile={}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile

user_profile = build_profile('sean','gill',
                             location='phoenix',
                             field = 'data science',
                             company='ports america',
                             wife='dinna',
                             oldest_son = 'connor',
                             youngest_son = 'bulldog')
print(user_profile)

# 8-14
def define_car(manufacturer, model,**car_info):
    car_detail={}
    car_detail['Manufacturer'] = manufacturer.title()
    car_detail['Model'] = model.title()
    for key, value in car_info.items():
        car_detail[key] = value.title()
    return car_detail

car_desc = define_car('ford','mustang',
                      doors = '2',
                      stereo = 'alpine',
                      wheels = '22-inch',
                      top = 'convertable')

print(car_desc)