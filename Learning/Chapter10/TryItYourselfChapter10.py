# 10-1
# read whole file
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

# read file per line
filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

# put file in list and read list - notice the FOR and PRINT are outside of the OPEN block
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# 10-2 using REPLACE
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip().replace('Python', 'C'))

# 10-3
prompt = input("What is your name: ")

with open('guest.txt', 'w') as file_object:
    file_object.write(prompt.title())

# 10-4
message = "Please enter your name."
message += "(Type 'q' to quit.)"

while True:
    prompt = input("What is your name: ")

    if prompt == 'q':
        break

    with open('guest_book.txt', 'a') as file_object:
        file_object.write(prompt.title() + "\n")

# 10-5 same as 10-4 with different prompt and input.
# 10-6
print("Give me two numbers and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can't add non numbers dumbass!")
    else:
        print(answer)


# 10-7 already did this as part of the 10-6 solution
# 10-8
def read_files(filename):
    """Method to read a file contents and print to screen"""

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("The file " + filename + " not found.")
    else:
        print(contents)


files = ['cats.txt', 'dogs.txt', 'scooby.txt']
for file in files:
    read_files(file)

# 10-9
def read_files(filename):
    """Method to read a file contents and print to screen"""

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


files = ['cats.txt', 'dogs.txt', 'scooby.txt']
for file in files:
    read_files(file)

# 10-10
def count_specific_word(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # count the number of words in the file
        words = contents.lower().split() # split uses spaces to seperate the words into a LIST
        num_word = words.count('time')
        print("The file " + filename + " has the spcified word " + str(num_word) + " times.")

filename = 'alice.txt'
count_specific_word(filename)

# add multiple files to the mix including one that does not exist to verify the try block
filenames = ['alice.txt','siddhartha.txt','ass_face.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_specific_word(filename)
