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
    index_list = make_index_list(input_text)
    base_word_list = make_base_word_list(file)
    encrypted_word_list = []
    i = 0
    for i in index_list:
        encrypted_word_list.append(base_word_list[i])
    encrypted_string=""
    for i in encrypted_word_list:
        encrypted_string = encrypted_string+i+" "

    return encrypted_string


print(encrypt("hello billy", "test_script.txt"))