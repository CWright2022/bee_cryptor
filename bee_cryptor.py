'''
Bee_cryptor: encrypt or decrypts text using a script (originally the Bee Movie script)
reborn from an old high school project
Cayden Wright 10/06/2022
'''
# amount of shift from first unicode character to the first one we actually want to use. Allows script to be smaller.
OFFSET = 32


def make_index_list(input_text):
    '''
    converts a string into a numeric list, with space being 0 and tilde being 94
    '''
    # make text into list of characters
    # convert each to unicode values
    input_list = list(input_text)
    for i in range(len(input_list)):
        char = ord(input_list[i])
        # subtract OFFSET, so that space is 0
        input_list[i] = char-OFFSET
    # return the changed list
    return input_list


def make_base_word_list(file):
    '''
    helper function that converts file to a list of unique words
    '''
    # put all words in list, skip any duplicates
    out_list = []
    with open(file) as file:
        for line in file:
            words = line.split()
            for word in words:
                #if word isn't already in list...
                if word not in out_list:
                    #and it's not a newline or CRLF...
                    if word != "\n" and word != "\r\n":
                        #then add it
                        out_list.append(word)
        return out_list


def encrypt(input_text, file):
    '''
    returns a big long string with each word from script separated by a space, given input text and the script
    '''
    # get list of input text
    index_list = make_index_list(input_text)
    # get base word list
    base_word_list = make_base_word_list(file)
    # for each in index_list, append to encrpyted_word list
    encrypted_word_list = []
    for i in index_list:
        try:
            encrypted_word_list.append(base_word_list[i])
        # if we find a character we don't know, insert a space
        except IndexError:
            print("skipping unknown character")
            encrypted_word_list.append(" ")

    # for each in word list, append to string
    encrypted_string = ""
    for i in encrypted_word_list:
        encrypted_string = encrypted_string+i+" "

    return encrypted_string

# make list from space separated string
# make numeric list from each word
# add OFFSET to each
# convert each back to unicode


def decrypt(input_text, file):
    '''
    makes list of index of each word (separated by space) of input text
    '''
    base_text_list = make_base_word_list(file)
    text_list = input_text.split()
    index_list = []
    # for each in text_list, add OFFSET to index and convert to unicode
    for i in text_list:
        try:
            index_list.append(chr((base_text_list.index(i))+OFFSET))
        except ValueError:
            print("Invalid token - ensure your input is correct")
    # then convert to string and return it
    output_string = ""
    for i in index_list:
        output_string = output_string+i

    return output_string


def main():
    wordlist = "script.txt"
    # print welcome
    print("Welcome to the Bee-Cryptor - an encryption standard for bees\nby Cayden Wright, written 10/6/22\n\n")
    while True:
        # prompt for choice
        user_choice = input(
            "type e to encrypt, d to decrypt, w to set wordlist (default is script.txt), or x to quit\n\n")
        # exit case
        if user_choice.lower() == "x":
            break
        # wordlist case
        elif user_choice.lower() == "w":
            wordlist = input("enter path to new wordlist:\n\n")
            # ensure file actually exists
            try:
                open(wordlist)
            except FileNotFoundError:
                print("File "+wordlist +
                      " not found. Ensure file exists and path is correct.")
                continue
            print("Wordlist set to:", wordlist)
        # encrypt case
        elif user_choice.lower() == "e":
            input_text = input("enter text to encrypt:\n")
            encrypted_text = encrypt(input_text, wordlist)
            print("Your encrypted text is:\n\n"+encrypted_text, end="\n\n")
            with open('output.txt', 'w') as file:
                file.write(encrypted_text)
        # decrypt case
        elif user_choice.lower() == "d":
            input_text = input("enter text to decrypt:\n")
            decrypted_text = decrypt(input_text, wordlist)
            print("Your decrypted text is:\n\n"+decrypted_text, end="\n\n")
            with open('output.txt', 'w') as file:
                file.write(decrypted_text)
        else:
            print("invalid input")


if __name__ == "__main__":
    main()
