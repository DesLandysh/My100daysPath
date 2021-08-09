# Caesar Cipher

def encrypt(base, txt, code):
    cipher_txt = ""
    for letter in txt:
        # index = base.index(letter)  # not used
        cipher_txt += base[base.index(letter) + code]
    print(f"The encoded text in {cipher_txt}")

alphabet = list("a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" "))

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# 1 Create a foo called 'encrypt that takes the 'text' and 'shift' as inputs.
#   2 Inside the this foo, shift each letter of the 'text' forward in the alphabet by the shift amount
#       and print the encrypted text.
#   text = "hello"
#   shift = 5
#   cipher_text = "mjqqt"
#   print output: "The encoded text is mjqqt"
# 3 Call the encrypt foo and pass in the user inputs. You shoout be able to text the code.
if direction == 'encode':
    encrypt(alphabet, text, shift)
else:
    pass
