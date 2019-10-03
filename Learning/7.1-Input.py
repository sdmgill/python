message = input("Tell me something and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello " + name.title())

# building a prompt over several lines
prompt = "This is going to be a very long way of asking "
prompt += "you what you name is. So..................."
prompt += "waht's your name?"

name = input(prompt)
print("Hello " +name.title())

# input returns everything as a string so we need to convert when evaluating numbers
height = input("How tall are you in inches?")
height = int(height)

if height > 36:
    print("\nYou are tall enough to ride!")
else:
    print("You are a small fucker!")

# Modulo
number = input("Enter a number and I will tell you if it is even or odd:")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")