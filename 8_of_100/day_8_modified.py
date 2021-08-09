# Caesar Cipher

def cipher(txt, code, sign):
    cipher_txt = ""
    for item in txt:  # improving to get the multiwords result
        for letter in item:
            if sign:
                cipher_txt += alphabet[(alphabet.index(letter) + code) % len(alphabet)]  # stolen variant (... % 26)
            else:
                cipher_txt += alphabet[alphabet.index(letter) - code % len(alphabet)]
        cipher_txt += " "  # multiword connector
    print(f"The encoded text is {cipher_txt}")


alphabet = list("a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" "))

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower().split()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    cipher(text, shift, True)
elif direction == 'decode':
    cipher(text, shift, False)
