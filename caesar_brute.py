import string
# from sys import argv
from langdetect import detect

# Based on : http://programeveryday.com/post/implementing-a-basic-caesar-cipher-in-python/

# Original code produced by:
__author__ = 'rahmaa'

# Multi lingual handeling and UI support produced by:
__coauthor__ = 'rjdoubleu' 

# Need to chnage to support UTF-8 encoding for special letters
alphabet = string.ascii_lowercase

supported_langauges = ['af', 'ar', 'bg', 'bn', 'ca', 'cs', 'cy', 
                       'da', 'de', 'el', 'en', 'es', 'et', 'fa', 
                       'fi', 'fr', 'gu', 'he', 'hi', 'hr', 'hu', 
                       'id', 'it', 'ja', 'kn', 'ko', 'lt', 'lv', 
                       'mk', 'ml', 'mr', 'ne', 'nl', 'no', 'pa', 
                       'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'so', 
                       'sq', 'sv', 'sw', 'ta', 'te', 'th', 'tl', 
                       'tr', 'uk', 'ur', 'vi', 'zh-cn', 'zh-tw']

#Encrypt the string and return the ciphertext
def encrypt(n, plaintext):
    result = ''
    for l in plaintext:
        try:
            index = alphabet.index(l.lower())
            i =  (index + n) % 26
            result += alphabet[i]
        except ValueError:
            result += l
    return result

#Decrypt the string and return the plaintext
def decrypt(ciphertext, target_language):
    dec = []
    detected_language = ''

    for n in range(0,26):
        result = ''
        for l in ciphertext:
            try:
                index = alphabet.index(l.lower())
                i =  (index - n) % 26
                result += alphabet[i]            
            except ValueError:
                result += l
        dec.append(result)
        detected_language = detect(dec[n])
        if detected_language == target_language or target_language == '':
            print('Language Detected:', detected_language)
            print('Decrypted Text:\n'+ dec[n]) 
            print('Ceaser Cipher Key:', n, '\n')
            return detected_language
    
    return detected_language

print("\n")
print("-" * 34)
print("- Caesar Cipher Brute Force" + " " * 5  + "-")
print("- Author: rhama.my.id" + " " * 11  + "-")
print("- Co Author: rjdoubleu" + " " * 10  + "-")
print("-" * 34)
while True:
    
    choice = input('\nChoose an option (encrypt, decrypt, quit) [e|d|q]: ').lower()
    
    if choice == 'e' or choice == 'encrypt':
        while True:
            msg = input('Enter the message you want to encrypt:\n')
            if msg == '':
                print('You didn\'t enter a message, please try again.')
            else:
                while True:
                    try:
                        key = int(input('Enter the key for your encryption: '))
                        break
                    except ValueError:
                        print('Sorry, I didn\'t understand the key you entered, please try again.')
                break
        print('Your encrypted message:\n'+ encrypt(key, msg))
    
    elif choice == 'd' or choice == 'decrypt':
        while True:
            msg = input('Enter the message you want to decrypt:\n')
            if msg == '':
                print('You didn\'t enter a message, please try again.')
            else:
                print('\nThe following languages are supported:\n' , *supported_langauges , '\n')
                while True:
                    lang = input('Please enter the language of the cipher text: ').lower()
                    if lang not in supported_langauges:
                        print('The language you entered is not currently supported, please try again.')
                    else:
                        break
                pred = decrypt(msg, lang)
                if pred != lang or pred =='':
                    print('Failed to decrypt the message. The message may be too short.')
                break
    elif choice == 'q' or choice =='quit':
        print('Goodbye')
        break
    else:
        print('Sorry I didn\'t understand your choice, please try again.')