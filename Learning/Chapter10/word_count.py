def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # count the number of words in the file
        words = contents.split() # split uses spaces to seperate the words into a LIST
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)

# add multiple files to the mix including one that does not exist to verify the try block
filenames = ['alice.txt','siddhartha.txt','ass_face.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)