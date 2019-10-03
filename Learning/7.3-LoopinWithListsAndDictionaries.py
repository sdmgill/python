# Moving Items from one list to another
unconfirmed_users=['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
    current_user=unconfirmed_users.pop()

    print("Verifiying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Remove all instances of specific values from a list
pets =['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling a dictionary with user input
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes / no)")
    if repeat == 'no':
        polling_active = False

print("\n --- Poll Results --- ")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")
