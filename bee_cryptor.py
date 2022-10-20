'''
Bee_cryptor: encrypt or decrypts text using a script (originally the Bee Movie script)
reborn from an old high school project
Cayden Wright 10/06/2022
'''
import argparse
from ast import arg
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
    # make sure list is long enough to contain all 94 possible characters
    with open(file) as file:
        for line in file:
            words = line.split()
            for word in words:
                # if word isn't already in list...
                if word not in out_list:
                    # and it's not a newline or CRLF...
                    if word != "\n" and word != "\r\n":
                        # then add it
                        out_list.append(word)
        return out_list


def read_from_file(file):
    '''
    helper function that returns a string separated by spaces, from a file. Useful for input that contains newlines.
    '''
    output_string = ""
    with open(file) as file:
        for line in file:
            line_list = line.split()
            for word in line_list:
                output_string = output_string+word+" "
    return output_string


def encrypt(input_text, file, from_file=False):
    '''
    returns a big long string with each word from script separated by a space,
    given input text and the script. if from_file=True, then it treats input_text
    as a filename to read from a file.
    '''
    # read from file, if applicable
    if from_file == True:
        try:
            input_text = read_from_file(input_text)
        except FileNotFoundError:
            print("file not found. using your filename as input text")
    # get list of input text
    index_list = make_index_list(input_text)
    # get base word list
    base_word_list = make_base_word_list(file)
    # ensure base word list is long enough for all 94 characters
    if len(base_word_list) < 94:
        print("ERROR: Word list not long enough. Wordlist must contain at least 94 words, separated by spaces.")
        return ""
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


def decrypt(input_text, file, from_file=False):
    '''
    makes list of index of each word (separated by space) of input text
    '''
    if from_file == True:
        try:
            input_text = read_from_file(input_text)
        except FileNotFoundError:
            print("file not found. using your filename as input text")
    base_text_list = make_base_word_list(file)
    # ensure base word list is long enough for all 94 characters
    if len(base_text_list) < 94:
        print("ERROR: Word list not long enough. Wordlist must contain at least 94 words, separated by spaces.")
        return ""
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


def run_interactive_mode():
    wordlist = "script.txt"
    # print welcome
    print("Welcome to the Bee-Cryptor - an encryption standard for bees\nby Cayden Wright, written 10/6/22\n\n")
    while True:
        # prompt for choice
        user_choice = input(
            "e - encrypt\nef - encrypt from file\nd - decrypt\ndf - decrypt from file\nw - change wordlist(default is script.txt)\nx - exit\n\n")
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
        # encrypt user input case
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
        # encrypt from file
        elif user_choice.lower() == "ef":
            input_text = input("enter input file name:\n")
            encrypted_text = encrypt(input_text, wordlist, True)
            print("Your encrypted text is:\n\n"+encrypted_text, end="\n\n")
            with open('output.txt', 'w') as file:
                file.write(encrypted_text)
        # decrypt from file
        elif user_choice.lower() == "df":
            input_text = input("enter input file name:\n")
            decrypted_text = decrypt(input_text, wordlist, True)
            print("Your decrypted text is:\n\n"+decrypted_text, end="\n\n")
            with open('output.txt', 'w') as file:
                file.write(decrypted_text)
        else:
            print("invalid input")


def parse_cli_arguments():
    '''
    returns "args", an object with methods (i think that's what they're called) corresponding to the value of each argument
    '''
    # setup arg_parser
    arg_parser = argparse.ArgumentParser()
    # you can't have multiple of these together
    enc_text_arg_group = arg_parser.add_mutually_exclusive_group()
    enc_text_arg_group.add_argument('-encrypt', type=str, help="text to encrypt")
    enc_text_arg_group.add_argument('-decrypt', type=str, help="text to decrypt")
    enc_text_arg_group.add_argument('-encrypt_file', type=str, help="file to encrypt from")
    enc_text_arg_group.add_argument('-decrypt_file', type=str, help="file to decrypt from")
    # but you can have the wordlist, so it doesn't get added to the group
    arg_parser.add_argument('-wordlist', type=str, help="file to use as wordlist", default="script.txt")
    args = arg_parser.parse_args()
    return args


def run_cli_argument_mode():
    '''
    runs in "CLI argument mode" - this function returns the output that would normally be printed to the user
    '''
    args = parse_cli_arguments()
    # encrypt case
    if args.encrypt:
        return (encrypt(args.encrypt, args.wordlist))


if __name__ == "__main__":
    args=parse_cli_arguments()
    if args.encrypt or args.decrypt or args.encrypt_file or args.decrypt_file:
        print(run_cli_argument_mode())
    else:
        run_interactive_mode()
