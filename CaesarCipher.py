def choose_method(method, character, shift):
    ascii_code = ord(character)
    if method == 'encrypt':
        number = ((ascii_code - 96) + shift) % 26
    elif method == 'decrypt':
        number = ((ascii_code - 96) - shift) % 26
    return chr(number + 96)


def caesar_cipher(method, sentence, shift):
    message = ''
    for letter in sentence:
        message += choose_method(method, letter, shift)
    return message


method_type = input("Would you like to encrypt or decrypt (Encrypt/Decrypt)? ").lower()
word = input("Enter your word? ").lower()
key = int(input("What is your key? "))

print(caesar_cipher(method_type, word, key))

