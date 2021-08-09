# Caesar Cipher

def encrypt(txt, code):
    cipher_txt = ""
    for item in txt:  # improving to get the multiwords result
        for letter in item:
            # cipher_txt += alphabet[alphabet.index(letter) + code - len(alphabet)]  # only for low numbers
            cipher_txt += alphabet[(alphabet.index(letter) + code) % len(alphabet)]  # stolen variant (... % 26)
        cipher_txt += " "  # multiword connector
    print(f"The encoded text is {cipher_txt}")

def decrypt(txt, code):
    cipher_txt = ""
    for item in txt:
        for letter in item:
            cipher_txt += alphabet[alphabet.index(letter) - code % len(alphabet)]
        cipher_txt += " "
    print(f"The decoded text is {cipher_txt}")



alphabet = list("a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" "))

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower().split()
shift = int(input("Type the shift number:\n"))

# 1 Create a foo called 'decrypt' that takes the 'text' and 'shift' as inputs.
#   2 Inside the this foo, shift each letter of the 'text' *backward* in the alphabet by the shift amount
#       and print the decrypted text.
#   cipher_text = "mjqqt"
#   shift = 5
#   text = "hello"
#   print output: "The encoded text is mjqqt"
# 3 Call the foo and pass in the user inputs. You should be able to text the code.
if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    pass
