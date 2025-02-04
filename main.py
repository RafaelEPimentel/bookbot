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


def sort_on(dict):
    return dict["num"]

#function that takes a dictionary with the information of how many characters in a book and an integer that holds the amount of words
def create_report(dict,numwords):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{numwords} words found in the document")
    print()
    #sort dictionary in descending order of character appearances
    dict_list = [{"num": dict[x],"char": x} for x in dict if x.isalpha()]
    dict_list.sort(reverse=True,key=sort_on)
    for dictionary in dict_list:
        print(f"The '{dictionary['char']}' character was found {dictionary['num']} times")
    print("--- End report ---")




def main():
    path = "books/frankenstein.txt"
    stringified_book = reader(path)
    words_counted = count_words(stringified_book)
    characters_counted = count_characters(stringified_book)
    #print(stringified_book)
    #print(words_counted)
    #print(characters_counted)
    create_report(characters_counted,words_counted)

main()
