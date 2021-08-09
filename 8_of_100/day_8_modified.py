# Caesar Cipher

def caesar(txt, code, sign):
    """
    Encode and decode the text by caesar cipher script
    :param txt: user text
    :param code: amount of shift
    :param sign: direction switcher
    :return: new text
    """
    cipher_txt = ""
    if sign == 'decode':
        code *= -1
    elif sign != 'decode' and sign != "encode":  # prevent mistyping
        print("Typed wrong command, Exiting...")
        return None
    for item in txt:  # improving to get the multi-words result
        for letter in item:
            cipher_txt += alphabet[(alphabet.index(letter) + code) % len(alphabet)]
        cipher_txt += " "  # multi-word connector
    print(f"The {sign}d text is {cipher_txt}")


alphabet = list("a b c d e f g h i j k l m n o p q r s t u v w x y z".split())

# User instructions
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower().split()
shift = int(input("Type the shift number:\n"))

# request to cipher function
caesar(text, shift, direction)
