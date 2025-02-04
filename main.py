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

#function that counts characters and return a dictionary with the result
def count_characters(string):
    #make string lowercase to avoid repeats
    string = string.lower()
    counter_dict = {}
    #loop through each character in string and either create a new key if the character is there already or add +1 to the counter
    for char in string:
        if char in counter_dict:
            counter_dict[char] = counter_dict[char] + 1
        else:
            counter_dict[char] = 1
    return counter_dict




def main():
    path = "books/frankenstein.txt"
    print(reader("books/frankenstein.txt"))
    print(count_words(reader(path)))
    print(count_characters(reader(path)))

main()
