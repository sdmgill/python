my_foods = ['pizza','falafel','carrot cake']
friends_food = my_foods[:] #slice includes the whol list in this case

print("My favorite foods are:")
print(my_foods)

print("\nMy Friend's favorite foods are:")
print(friends_food)

# make some mods just to verify that we are using 2 different lists from above example
my_foods2 = ['pizza','falafel','carrot cake']
friends_food2 = my_foods2[:] #slice includes the whol list in this case

my_foods2.append('cannoli')
friends_food2.append('shit sandwich')

print("\nMy favorite foods are:")
print(my_foods2)

print("\nMy Friend's favorite foods are:")
print(friends_food2)
