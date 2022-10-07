'''
Bee_cryptor: encrypt or decrypts text using a script (originally the Bee Movie script)
reborn from an old high school project
Cayden Wright 10/06/2022
'''


def make_index_list(input_text):
    '''
    converts a string into a numeric list, with space being 0 and tilde being 94
    '''
    # make text into list of characters
    # convert each to unicode values
    input_list = list(input_text)
    for i in range(len(input_list)):
        char = ord(input_list[i])
        # subtract 32, so that space is 0
        input_list[i] = char-32
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
                if word not in out_list:
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
        encrypted_word_list.append(base_word_list[i])
    # for each in word list, append to string
    encrypted_string = ""
    for i in encrypted_word_list:
        encrypted_string = encrypted_string+i+" "

    return encrypted_string

# make list from space separated string
# make numeric list from each word
# add 32 to each
# convert each back to unicode


def decrypt(input_text, file):
    '''
    makes list of index of each word (separated by space) of input text
    '''
    base_text_list=make_base_word_list(file)
    text_list = input_text.split()
    index_list = []
    # for each in text_list, add 32 to index and convert to unicode
    for i in text_list:
        index_list.append(chr((base_text_list.index(i))+32))
    #then convert to string and return it
    output_string = ""
    for i in index_list:
        output_string = output_string+i

    return output_string


# right? coworkers back back afterwards
print(decrypt("right? coworkers back back afterwards", "test_script.txt"))
