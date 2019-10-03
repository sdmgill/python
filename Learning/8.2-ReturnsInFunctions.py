def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendricks')
print(musician)

# optional arguments - essentially placing an empty default
def get_formatted_name(first_name,last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendricks')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)

# returning a dictionary
def build_person(first_name, last_name):
    """Returns a dictionary"""
    person = {'first':first_name,'last':last_name}
    return person

musician = build_person('jimi','hendricks')
print(musician)

# add to the dictionary
def build_person(first_name, last_name, age=''):
    """Returns a dictionary"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendricks')
print(musician)

musician = build_person('jimi','hendricks',27)
print(musician)

# using a Function in a while loop
def another_formatted_name(first_name, last_name):
    """Return a neatly formatted name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name. ")
    print("(Enter 'q' at any time to exit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = another_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")