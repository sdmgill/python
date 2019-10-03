# simple WHILE loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# keep looping until the user exits with "quit". Issue here is that 'quit' is printed at the end
prompt = ("\nHELL me something and I will repeat it back to you: ")
prompt += ("\nEnter 'quit' to end the program.")

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# keep looping until the user exits with "quit". If statement at the bottom prevents the 'quit' from being printed.
prompt = ("\nTELL me something and I will repeat it back to you: ")
prompt += ("\nEnter 'quit' to end the program.")

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# use a flag to exit the loop
prompt = ("\nSMELL me something and I will repeat it back to you: ")
prompt += ("\nEnter 'quit' to end the program.")

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# use a BREAK to exit the loop
prompt = ("\nPlease enter the name of a city you have visited: ")
prompt += ("\nEnter 'quit' to end the program.")

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("\nI'd love to go to " + city.title() + "!")

# using CONTINUE in a loop
current_number = 0
while current_number <10:
    current_number +=1
    if current_number % 2 == 0:
        continue

    print(current_number)