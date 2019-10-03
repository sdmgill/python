# multiple "IF" statements will continue to process through to the end even if the first condition is satisfied

requested_topping = ['mushrooms','extra cheese','ass lint']

if 'mushrooms' in requested_topping:
	print("Adding mushrooms")
if 'pepperoni' in requested_topping:
	print("Adding pepperoni")
if 'extra cheese' in requested_topping:
	print("Adding extra cheese")
	
print("\nFinished making your pizza!")
