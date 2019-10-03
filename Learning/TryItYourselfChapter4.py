#4-1
print('"4-1 Pizzas"')
pizzas = ['pepperoni','sausage','garbage']
for pizza in pizzas:
	print(pizza)
	print("I like " + pizza + " pizza.\n")
	
print("Loving pizza outide da' loop")

#4-3
print('\n"4-3 Counting to 20"')
for value in range(1,21):
	print (value)
	
#4-4

#print('\n"4-4 Counting to 1 mil using a list"')
#mil = []
#for value in range(1,1000001):
#	mil = value
#	print(mil)
	
#4-5
print('\n"4-5 Summing a Million"')
mil = list(range(1,1000001))
#print (mil)
print (min(mil))
print (max(mil))
print (sum(mil))

#4-6
print('\n"4-6 Odd Numbers"')
for value in range(1,20,2):
	print (value)
	
#4-7
print('\n"4-7 Multiples of 3"')
multiples=[]
for value in range(1,11):
	multiply = value*3 
	multiples.append(multiply)
print(multiples)	

#4-8
print('\n"4-8 Cubes"')
cubes=[]
for value in range(1,11):
	cube = value**3 # ** = exponent
	cubes.append(cube)
print(cubes)

#4-9
print('\n"4-9 Cubes using a list comprehension"')
cubes=[value**3 for value in range(1,11)]
print (cubes)

#4-10 
print('\n"4-10 Slices"')
enemies = ['darkseid','thanos','green hornet','hela','dark elves']
print("The first three enemies are:")
for enemy in enemies[:3]:
	print(enemy.title())
	
print("\nThe middle 3 enemies are:")
for enemy in enemies[1:4]:
	print(enemy.title())
	
print("\nThe last 3 enemies are:")
for enemy in enemies[-3:]:
	print(enemy.title())
	
#4-11
print('\n"4-10 Pizza Shit"')
pizzas = ['pepperoni','sausage','garbage']
friends_pizza = pizzas[:] #copy the list into another

pizzas.append('cheese')
friends_pizza.append('ass pie')

print("\nMy favorite pizzas are:")
print(pizzas)

print("\nMy Friend's favorite pizzas are:")
print(friends_pizza)



