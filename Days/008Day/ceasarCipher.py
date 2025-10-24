import art

def caesar(direction,original_text,shift_amount) :
    if direction == 'encode' :
        #print(f"encode : shift amount {shift_amount}")
        encrypt(original_text=original_text,shift_amount=shift_amount)
    elif direction == 'decode' : 
        decrypt(original_text=original_text,shift_amount=shift_amount)

def encrypt(original_text,shift_amount) :
    cipher_text =""

    for letter in original_text.lower() :
        if 'a' <= letter <= 'z':
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)    #   makes sure that we are between 0-25
            cipher_text += alphabet[shifted_position]
        else :
            cipher_text += letter
    print(f"Encripted word is {cipher_text}") 

def decrypt(original_text,shift_amount) :
    cipher_text = ""

    for letter in original_text.lower() : 
        if 'a' <= letter <= 'z' :
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        else :
            cipher_text += letter
    print(f"Decrypted word is {cipher_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
restart = 'yes'

while restart == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(direction=direction.lower(),original_text=text,shift_amount=shift)

    restart = input("Would you like to restart cipher program? (yes or no)\n")