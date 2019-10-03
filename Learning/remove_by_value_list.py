#remove by value list --like pop we can use the value after it has been removed
print("")
print("'remove by value list'")
motorcycles =['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
print("\n")
