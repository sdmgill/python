#sorting lists "sort" changes the list itself and cannot be reverted unless you manually go back and change shit
cars = ['bmw','audi','toyota','subaru']
print("'pre-sort'")
print(cars)
print("\n")

print("'post-sort'")
cars.sort()
print(cars)
print("\n")

#reverse sorting -->this reverses the sort alphabetically
print("'reverse -sort'")
cars.sort(reverse=True)
print(cars)
print("\n")

#"sorted" changes the list temporarily and then reverts back to the original order
cars = ['bmw','audi','toyota','subaru']
print("'Here is the original list'")
print(cars)

print("\n'Here is the temp sorted list'")
print(sorted(cars))
print("\n'Back to the original order'")
print(cars)

#reversing the order --> this just flips the list order and does not arrange alphbetically
cars = ['bmw','audi','toyota','subaru']
print("\n'Here is the original list'")
print(cars)

print("\n'Let's flip this bitch'")
cars.reverse()
print(cars)



