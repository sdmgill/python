#putting a range into a list for simple math
print("Here is my range placed into a list for simple math:")
squares=[]
for value in range(1,11):
	square = value**2 # ** = exponent
	squares.append(square)
	
print(squares)

#simpler version
print("\nHere is my range placed into a list for simple math (concise code):")
squares=[]
for value in range(1,11):
	squares.append(value**2)
	
print(squares)

#simple stats
print("\nUsing a list for simple stats:")
digits =[0,1,2,3,4,5,6,7,8,9]
print("\nMy List")
print(digits)

print("\nMIN")
print(min(digits))

print("\nMAX")
print(max(digits))

print("\nSUM")
print(sum(digits))

# using a list comprehension
print("\nList Comprehension")
squares=[value**2 for value in range(1,11)]
print (squares)
