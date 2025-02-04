
def reader(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(reader("books/frankenstein.txt"))

main()
