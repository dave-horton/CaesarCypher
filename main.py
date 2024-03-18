import string
alphabet = list(string.ascii_lowercase) #Get lower case alphabet as a list

#Define caesar function that encrypts or decrypts message based on the cipher direction and shift amount provided.
def caesar(plain_text, shift_amount, cipher_direction):  
    cipher_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
           position = alphabet.index(char)
           new_position = (position + shift_amount) % len(alphabet)
           cipher_text +=alphabet[new_position]
        else:
            cipher_text += char
    print(f"The {cipher_direction}d text is {cipher_text}")

#Loop until user wants to quit program
running = True
while running:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") #Verify 'encode' or 'decode' from user.
        if direction.lower() not in ('encode','decode'):
            continue
        else:
            break

    text = input("Type your message:\n").lower() #Get message from user.

    shift = None
    while shift is None:
        try:
            shift = int(input("Type the shift number:\n")) #Get integer input.
        except:
            print("Try again.")

    caesar(plain_text=text,shift_amount=shift,cipher_direction=direction) #Call caesar function

    go_again = input("Type 'yes' if you want to go again.\n") #Ask if user wants to run program again.
    if go_again.lower() != 'yes':
        running = False
        print("Goodbye!")


