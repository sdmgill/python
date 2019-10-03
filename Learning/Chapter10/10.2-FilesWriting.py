# write a single line
filename = 'programming.txt'

"""
Can us r = read (default).
w = write (overwrite if exists).
r+ = read and write.
a = append (create if not exists). 
"a" is best when you need to write
"""
with open(filename,'w') as file_object:
    file_object.write("I love programming.")

# write multiple lines - writes both on the same line
filename = 'programming.txt'

"""
Can us r = read (default).
w = write (overwrite if exists).
r+ = read and write.
a = append (create if not exists). 
"a" is best when you need to write
"""
with open(filename,'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games")

# write multiple lines - writes on different lines
filename = 'programming.txt'

"""
Can us r = read (default).
w = write (overwrite if exists).
r+ = read and write.
a = append (create if not exists). 
"a" is best when you need to write
"""
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")


# append lines
filename = 'programming.txt'

"""
Can us r = read (default).
w = write (overwrite if exists).
r+ = read and write.
a = append (create if not exists). 
"a" is best when you need to write
"""
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I also love creating apps that can run in a browser.\n")


