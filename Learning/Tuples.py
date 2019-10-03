#whaddup tup? tuples are immutable (i.e. cannot be changed) lists
dimensions=(200,50) #use parentheses instead of brackets for tuples
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250 # this will throw an error since we cannot change a tuple

print("\nUse a loop to list the tuple values.")
for dimension in dimensions:
	print(dimension)
	
print("\nModify the variable that contains the tuple to 'modify the tuple'")
print("\nOriginal dimension (aka variable)")
for dimension in dimensions:
	print(dimension)
	
dimensions =(400,100) #reset the variable here therefore resetting the tuple inside
print("\nModified dimension (aka variable)")
for dimension in dimensions:
	print(dimension)
	




