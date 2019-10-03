# 7-1
car_type = input("What kind of car would you like to rent? ")
print("Let me see if I can find you a " + car_type.title() + ".")

# 7-2
party_size = input("How many people are in your party tonight? ")
party_size = int(party_size)
if party_size >8:
    print("\nThere will be a 20 minute wait while we prepare your table.")
else:
    print("\nPlease follow me.")

# 7-3
is10 = input("Tell me a number and I'll tell you if it is divisable by 10. ")
is10 = int(is10)
if is10 % 10 == 0:
    print("\nIt is!")
else:
    print("\nIt ain't.")

# 7-4
prompt =("\nWhat toppings would you like on your pizza? ")
prompt +=("Type 'Place Order' when finished. ")

message = ""

active = True
while active:
    message = input(prompt)

    if message == 'Place Order':
        active = False
        print("\nOrder Placed")
    else:
        print(message)

# 7-5
prompt =("\nHow old is the person for which you are purchasing the ticket? ")
message = input(prompt)
message = int(message)

if message < 3:
    print("Tickets for children under 3 are free. ")
elif message >=3 and message <=12:
    print("Your ticket is $10. ")
elif message > 12:
    print("Your ticket is $15")

# 7-6.1
prompt =("\nWhat toppings would you like on your pizza? ")
prompt +=("Type 'Place Order' when finished. ")


while True:
    message = ""
    message = input(prompt)
    if message == 'Place Order':
        print("\nOrder Placed")
        break
    else:
        print(message.title())
# 7-6.2
prompt =("\nWhat toppings would you like on your pizza? ")
prompt +=("Type 'Place Order' when finished. ")
message = ""

while message != "Place Order":
    message = input(prompt)

    if message != "Place Order":
    print(message.title())
else:
    print("\nOrder Placed")

# 7-7 Not done

# 7-8
sandwich_orders =['meatball','club','turkey']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I made your " + current_sandwich + " sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been prepared:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 7-9
sandwich_orders =['pastrami','meatball','pastrami','club','tuna','turkey','pastrami']
finished_sandwiches = []

if 'pastrami' in sandwich_orders:
    print("\nSorry, we are out of pastrami today.")

    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
print("\nUpdated sandwich order: ")

for order in sandwich_orders:
    print(order.title())

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I made your " + current_sandwich + " sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been prepared:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 7-10
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name]= response

    repeat = input("Would you like to let another person input their information? (yes / no) ")
    if repeat == 'no':
        polling_active = False

print("\n----- Polling Results -----")
for name, response in responses.items():
    print(name.title() + " would like to go to " + response.title() + "." )

