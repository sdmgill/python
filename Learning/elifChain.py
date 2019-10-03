# in an "elif" chain, once a condition has been met, the underlying code is executed and the program exits
# i.e. can only be used to pass a single condition.

age=3
if age <4:
	print("Your admission cost is $0")
elif age < 18:
	print("Your admission cost is $5")
else:
	print("Your admission cost is $10")

# more concise way to code the above
age = 18
if age <4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
	
print("\nYour admission cost is $" + str(price)+ ".")

# python does not require the final "else" and can chain "elif" statements as needed
age = 66
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5
	
print("\nYour admission cost is $" + str(price)+ ".")

