#simple list get everything from the list and then just the first record
bicycles = ['trek','cannondale','redline','specialized']
print("'simple list get everything from the list and then just the first record'")
print(bicycles)
print(bicycles[0])
print(bicycles[0].title() + "\n")

#get the last item in the list
print("'get the last item in the list'")
print(bicycles[-1])
print(bicycles[-1].title() + "\n")

#get the second to last item in the list
print("'get the second to last item in the list'")
print(bicycles[-2])
print(bicycles[-2].title() + "\n")

#get other records
print("'get other records'")
print(bicycles[1])
print(bicycles[2] + "\n")

#use in a message
print("'use in a message'")
message = "My first bicycle was a " + bicycles[2].title() + "."
print(message)



