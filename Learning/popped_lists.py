#using default 'pop' --takes the last record from the list
print("")
print('"using default "pop" --takes the last record from the list"')
motorcycles =['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)
print(motorcycles)
print("\n")

#reset with append
print("'reset with append'")
motorcycles.append('suzuki')
print(motorcycles)
print("\n")

#'pop' second record
print('" "pop" second record"')
popped2_motorcycle = motorcycles.pop(1)
print(popped2_motorcycle)
print(motorcycles)
print("\n")

#reset with insert
print("'reset with insert'")
motorcycles.insert(1,'yamaha')
print(motorcycles)
print("\n")
