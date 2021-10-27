# Here I dedicate to make a version of cipher of Caesar.
# This programa will be input a text and transposition value.
# By @jszvitor. Oriented by Don't Repeat Yourself(DRY) principle.

import sys # standard system library - user provides script commands via terminal or cmd
from string import ascii_lowercase as ALPHABET # library for string - we'll get the alphabet


def cipher(message, dir, rot):
    """
    This function take a argument 'message' and, based in argument 'dir',
    performs an encryption or decryption operation with the rotation provided by 'rot' argument.
    Finally, will return the ciphered message.
    """
    m = '' # ciphered message
    for caracter in message:
        if caracter in ALPHABET:
            caracter_index = ALPHABET.index(caracter)
            m += ALPHABET[(caracter_index +(dir*rot)) % 26]
        else:
            m += caracter
    return m

def encrypt(message, rot):
    return cipher(message, 1, rot)

def decrypt(message, rot):
    return cipher(message, -1, rot)

def main():
    command = sys.argv[1].lower()
    message = sys.argv[2].lower()
    rot = int(sys.argv[3])

    if command == 'encrypt':
        print(encrypt(message, rot))
    elif command == 'decrypt':
        print(decrypt(message, rot))
    else:
        print(command + ' -> command not found')

if __name__ == '__main__':
    main()

# For execute this program:
# command: encrypt or decrypt
# message: string
# rot: integer
# $ python3 CipherOfCaesar.py command message rot
# >>>
# exemple:
# $ python3 CipherOfCaesar.py encrypt 'abc' 1
# >>> bcd
# $ python3 CipherOfCaesar.py decrypt 'bcd' 1
# >>> abc