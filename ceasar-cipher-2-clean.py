from turtle import position


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encypted_text = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            index += shift
            if index >= len(alphabet):
                index -= len(alphabet)
            encypted_text += alphabet[index]
    print("The encoded text is " + encypted_text)

def decrypt(cipher_text, shift_amount):
    plain_text =""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if new_position < 0:
            new_position += len(alphabet)
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)