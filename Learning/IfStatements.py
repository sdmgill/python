cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'

if car == 'audi':
	print("\nIt does")
else:
	print("\nIt does not")


requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("\nPlease hold the anchovies")


banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print("\n" + user.title() + ", you can post a response if you wish.")
