# bee_cryptor
A fun project re-born from an old HS project. Encrypts text using the Bee Movie script (or any other multi-line) text of your choosing. Also the much better successor to bcrypt.

## Usage
Run bee_cryptor.py. When prompted, type e to encrypt, d to decrypt, w to change wordlist, or x to exit. PLEASE NOTE: sometimes copy-pasting text does not work due to Windows or another program adding newlines, causing the decryption process to end early (only decrypts part of your text). To get around this, bee_cryptor will also store the most recent output in output.txt (generated in the same directory as bee_cryptor.py) to enable better copy/pasting.