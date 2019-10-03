# generate an error - can't divide by 0
print(5/0)

# use try/except block to handle to error
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by 0 dumbass.")

# add to this
print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0 dumbass!")
    else:
        print(answer)

# generate an error - file not found
filename = 'alice.txt'

with open(filename) as f_obj:
    contents = f_obj.read()

# add exception handling
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)