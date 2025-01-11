
number_of_words = 0

# Opening our text file in read only
# mode using the open() function
with open(r'SampleFile.txt','r') as file:

    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()

    # Splitting the data into separate lines
    # using the split() function
    lines = data.split()

    # Iterating over every word in
    # lines
    for word in lines:

        # checking if the word is numeric or not
        if not word.isnumeric():          

            # Adding the length of the
            # lines in our number_of_words
            # variable
            number_of_words += 1

# Printing total number of words
print(number_of_words)
