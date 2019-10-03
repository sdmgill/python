#modifying lists
print("simple list")
motorcycles =['honda','yamaha','suzuki']
print(motorcycles)
print("\n")

#update the first record
print("update the first record")
motorcycles[0]='ducati'
print(motorcycles)
print("\n")

#set it back
print("set it back")
motorcycles[0]='honda'
print(motorcycles)
print("\n")

#add a record
print("add a record")
motorcycles.append('ducati')
print(motorcycles)
print("\n")

#start from an empty list
print("start from an empty list")
motorcycles =[]
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('susuki')
print(motorcycles)
print("\n")

#insert a new record to the beginning of the list
print("insert a new record to the beginning of the list")
motorcycles.insert(0, 'ducati')
print(motorcycles)
print("\n")

#delete the first record from the list
print("delete the first record from the list")
del motorcycles[0]
print(motorcycles)
print("\n")

#delete the second record from the list
print("delete the second record from the list")
del motorcycles[1]
print(motorcycles)
print("\n")

#reset with inserts
print("reset with inserts")
motorcycles.insert(0, 'ducati')
motorcycles.insert(2,'yamaha')
print(motorcycles)
print("\n")


