'''
Bee_cryptor: encrypt or decrypts text using a script (originally the Bee Movie script)
reborn from an old high school project
Cayden Wright 10/06/2022
'''
import argparse
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


def encrypt(input_text, file):
    '''
    returns a big long string with each word from script separated by a space,
    given input text and the script. if from_file=True, then it treats input_text
    as a filename to read from a file.
    '''
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
            print("skipping unknown character - using a space instead")
            encrypted_word_list.append(" ")

    # for each in word list, append to string
    encrypted_string = ""
    for i in encrypted_word_list:
        encrypted_string = encrypted_string+i+" "

    return encrypted_string


def decrypt(input_text, file):
    '''
    returns decrypted string given an input string and wordlist (file)
    '''
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
            print("error decrypting - ensure you have the correct wordlist and input")
    # then convert to string and return it
    output_string = ""
    for i in index_list:
        output_string = output_string+i

    return output_string


def encrypt_from_file(file, wordlist):
    '''
    encrypt from a file, given a wordlist
    '''
    # get text from file
    string_to_encrypt = ""
    with open(file) as file:
        for line in file:
            line_list = line.split()
            for word in line_list:
                string_to_encrypt = string_to_encrypt+word+" "
    # encrypt it
    return encrypt(string_to_encrypt, wordlist)


def decrypt_from_file(file, wordlist):
    '''
    decrypt from a file, given a wordlist
    '''
    # get text from file
    string_to_decrypt = ""
    with open(file) as file:
        for line in file:
            line_list = line.split()
            for word in line_list:
                string_to_decrypt = string_to_decrypt+word+" "
    # decrypt it
    return decrypt(string_to_decrypt, wordlist)


def parse_cli_arguments():
    '''
    returns "args", an object with methods (i think that's what they're called) corresponding to the value of each argument
    '''
    # setup arg_parser
    arg_parser = argparse.ArgumentParser()
    # you can't have multiple of these together
    enc_text_arg_group = arg_parser.add_mutually_exclusive_group()
    enc_text_arg_group.add_argument('-encrypt', type=str, help="encrypt from text")
    enc_text_arg_group.add_argument('-decrypt', type=str, help="decrypt from text")
    enc_text_arg_group.add_argument('-encrypt_file', type=str, help="encrypt from file")
    enc_text_arg_group.add_argument('-decrypt_file', type=str, help="decrypt from file")
    # but you can have -wordlist and -output, so it doesn't get added to the group
    arg_parser.add_argument('-wordlist', type=str, help="file to use as wordlist (default is ./script.txt)", default="script.txt")
    arg_parser.add_argument('-out_file', type=str,help="file to write output to, if any. Default just prints to terminal")
    args = arg_parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_cli_arguments()
    wordlist = args.wordlist
    #if we have a file output, then just write to file
    if args.out_file:
        out_file=args.out_file
        output=""
        if args.encrypt:
            output=encrypt(args.encrypt, wordlist)
        elif args.decrypt:
            output=decrypt(args.decrypt, wordlist)
        elif args.encrypt_file:
            output=encrypt_from_file(args.encrypt_file, wordlist)
        elif args.decrypt_file:
            output=decrypt_from_file(args.decrypt_file, wordlist)
        #write to file here
        with open(out_file, 'w') as output_file:
            output_file.write(output)
    #otherwise just print to terminal
    else:
        if args.encrypt:
            print(encrypt(args.encrypt, wordlist))
        elif args.decrypt:
            print(decrypt(args.decrypt, wordlist))
        elif args.encrypt_file:
            print(encrypt_from_file(args.encrypt_file, wordlist))
        elif args.decrypt_file:
            print(decrypt_from_file(args.decrypt_file, wordlist))
        else:
            print("no valid arguments")
