from math import log

def encode(message, cipher_alphabet):
    real_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher = dict()
    for index, letter in enumerate(real_alphabet):
        cipher[letter] = cipher_alphabet[index]
    message = message.upper()
    encoded = ""
    for letter in message:
        if letter in real_alphabet:
            encoded += cipher[letter]
        else:
            encoded += letter
    return encoded

def decode(message, cipher_alphabet):
    real_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher = dict()
    for index, letter in enumerate(cipher_alphabet):
        cipher[letter] = real_alphabet[index]
    message = message.upper()
    decoded = ""
    for letter in message:
        if letter in real_alphabet:
            decoded += cipher[letter]
        else:
            decoded += letter
    return decoded

