alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
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
            #print(index)
    print("The encoded text is " + encypted_text)


encrypt(text, shift)