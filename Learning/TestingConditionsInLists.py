print('"All toppings are in stock"')
requested_toppings = ["mushrooms","green peppers","extra cheese"]

for requested_topping in requested_toppings:
	print("Adding " + requested_topping + ".")
	
print("\nFinished making your pizza.")

# Oh no! we ran out of something
print('\n"All toppings are not in stock"')
requested_toppings = ["mushrooms","green peppers","extra cheese"]

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we ran out of " + requested_topping + ". Better luck next time.")
	else:
		print("Adding " + requested_topping + ".")
	
print("\nFinished making your pizza.")

# getting fancy....not in book
print('\n"All toppings are not in stock"')
requested_toppings = ["mushrooms","green peppers","extra cheese"]
out_of_stock = ['green peppers'] #put out of stock items into a list
out_of_stock.append('extra cheese') #add extra cheese to the out of stock list

for requested_topping in requested_toppings:
	if requested_topping in out_of_stock:
		print("Sorry, we ran out of " + requested_topping + ". Better luck next time.")
	else:
		print("Adding " + requested_topping + ".")
	
print("\nFinished making your pizza.")

#checking for an empty list
print('\n"Checking for an empty list"')
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping	+ ".")
	print("\nFinished making your pizza.")
else:
	print("Are you sure you want a plain pizza?")
	
#using multiple lists...already beat the books:)
print('\n"Using multiple lists"')
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
		
print("\nFinished making your pizza.")

#using multiple lists...adding another list not in book
print('\n"Using multiple lists"')
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese','green peppers']
out_of_stock = ['green peppers'] #put out of stock items into a list
for requested_topping in requested_toppings:
	if requested_topping in out_of_stock:
		print("Sorry, we ran out of " + requested_topping + ".")
	if requested_topping in available_toppings and requested_topping not in out_of_stock:
		print("Adding " + requested_topping + ".")
	if requested_topping not in available_toppings:
		print("Sorry, we don't add " + requested_topping + " to pizza. Freak!")
		
print("\nFinished making your pizza.")
