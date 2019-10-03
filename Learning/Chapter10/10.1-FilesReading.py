# file_reader.py V1
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# file_reader.py V2
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

# file_reader.py V3 remove blank lines between lines using rstrip
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

"""
Making a list of lines from a file.
when you execute open() the data is only available inside the block unless you throw it into a list
"""
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# move the lines onto a single line
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# move the lines onto a single line but get rid of all whitespace
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip() # change rstrip to strip

print(pi_string)
print(len(pi_string))

# same thing as above but for a larger file
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip() # change rstrip to strip

print(pi_string[:52] + "...") # only want t0 display the first 52
print(len(pi_string))  # verify that there is 1mil digits

