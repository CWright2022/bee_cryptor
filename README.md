# **bee_cryptor - the latest encryption standard for bees**
A fun project re-born from an old HS project. Encrypts text using the Bee Movie script (or any other multi-line) text of your choosing. Also the much better successor to bcrypt.

## **Usage**
Run bee_cryptor.py to be presented with a very basic CLI. Basic form is to enter an option, then enter input.
-h, --help                  show help message and exit
-encrypt (TEXT)             text to encrypt  
-decrypt (TEXT)             text to decrypt  
-encrypt_file (FILE_PATH)   file to encrypt from  
-decrypt_file (FILE_PATH)   file to decrypt from
-wordlist (FILE_PATH)       file to use as wordlist
### **Options**
#### -encrypt (TEXT) --- encrypts from CLI-given text
Uses the encrypt() function to encrypt user input using the specified wordlist (if no wordlist specified, defaults to ./script.txt).  
PLEASE NOTE: any input with spaces must be contained in quotation marks, and any input containing quotation marks must have an escape character before them (backslach \)  
EXAMPLE: `python bee_cryptor.py -encrypt "James said, \"Hello"\"`  
You may see an error such as `skipping unknown character - using a space instead`, this means that your input contains characters that bee_cryptor does not recognize. It will simply substitute a space in place of the unknown character.

#### -decrypt (TEXT) --- decrypts from CLI-given text
Uses the decrypt() function to decrypt user input using the specified wordlist (if no wordlist specified, defaults to ./script.txt).  
Once again, any input with spaces must be contained in quotation marks, and any input containing quotation marks must have an escape character before them (see example in -encrypt)  
If this function gives an error like `error decrypting - ensure you have the correct wordlist and input`, ensure that you do indeed have the correct input and wordlist - this error means that bee_cryptor was unable to decrypt that specific character, either because it was not found in the wordlist, or because it converts to an invalid character.

#### -encrypt_from_file (FILE_PATH) --- encrypts from text in a file
Uses the encrypt_from_file() function to encrypt text from a file using the specified wordlist (if no wordlist specified, defaults to ./script.txt). Files with spaces or quotations need to be handled slightly differently, see example above.  
FILE_NAME must be a .txt file.  
EXAMPLE: python bee_cryptor.py -encrypt_from_file my_input.txt

#### -decrypt_from_file (FILE_PATH) --- decrypts from text in a file
Uses the decrypt_from_file() function to decrypt text from a file using the specified wordlist (if no wordlist specified, defaults to ./script.txt). Files with spaces or quotations need to be handled slightly differently, see example above.  
FILE_NAME must be a .txt file.  
EXAMPLE: python bee_cryptor.py -decrypt_from_file my_input.txt

#### -wordlist (FILE_PATH) --- used in combination with other commands to set wordlist
This option specifies a different word list to use, rather than the provided default Bee Movie Script (script.txt). Wordlists must be at least 94 words long, space-separated, .txt files. Otherwise, you may see errors such as `ERROR: Word list not long enough. Wordlist must contain at least 94 words, separated by spaces.`.  
Example: `python bee_cryptor.py -encrypt "secret message" -wordlist "emancipation_proclamation.txt"`  

#### -out_file (FILE_PATH) --- used to set output file
Use this option to have bee_cryptor output to a file rather than the terminal by specifying a file path.  
EXAMPLE: `python bee_cryptor.py -encrypt "secret message" -out_file secret.txt`  
NOTE: when this option is in use, nothing will be printed to the terminal.