#find list length --> this is a bit misleading as it return the count of items in the list not necessarily the actual length
cars = ['bmw','audi','toyota','subaru']
print('"Original list"')
print(cars)
print(len(cars))

print('\n"Remove one"')
del cars[1]
print(cars)
print(len(cars))

print('\n"Append one"')
cars.append('audi')
print(cars)
print(len(cars))

print('\n"Try to pop it out and then back in but in the original order"')
popped_cars = cars.pop()
cars.insert(1,popped_cars)
print(cars)
print(len(cars))

print('\n"Append one more for giggles"')
cars.append('jalopy')
print(cars)
print(len(cars))
