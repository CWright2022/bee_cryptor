'''
Bee_cryptor: encrypt or decrypts text using a script (originally the Bee Movie script)
reborn from an old high school project
Cayden Wright 10/06/2022
'''

def convert_to_index_list(input_text):
    '''
    converts a string into a numeric list, with space being 0 and tilde being 94
    '''
    #make text into list of characters
    #convert each to unicode values
    input_list=list(input_text)
    for i in range (len(input_list)):
        char = ord(input_list[i])
        #32 is the offset (to make space 0)
        input_list[i]=char-32
    #return the changed list
    return input_list


def encrypt(text, file):
    '''
    encrypts text using file
    '''
