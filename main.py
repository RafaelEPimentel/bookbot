#Function that takes in a file, reads it and returns it as a string
def reader(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

#Function that counts the words in a string and returns the result
def count_words(string):
    counter = 0
    split_string = string.split()

    for word in split_string:
        counter += 1
    return counter



def main():
    print(reader("books/frankenstein.txt"))
    print(count_words(reader("books/frankenstein.txt")))

main()
