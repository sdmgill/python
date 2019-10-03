#looping in lists
magicians =['sean','dinna','connor','bulldog']
print("Here is my list:")
print(magicians)
print("\n")
#magicians = sorted(magicians)
print("Here are the results of the loop:")
for magician in magicians:
	print(magician.title())

#doing more than one thing in the loop
print("\n")
print("'Doing more than one thing inside the loop'")
for magician in magicians:
	print(magician.title() + ", that was a great trick.")
	print("Now go make your ass disappear, " + magician.title() + "!\n")
print("I didn't indent so Python threw this out of the loop.")
	

