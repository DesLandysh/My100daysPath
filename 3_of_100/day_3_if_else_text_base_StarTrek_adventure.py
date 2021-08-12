# Text_base_if/else game
print("""
***********************************************************************
      _____________________________________________________________
     /          _____             __   __       ___  __       ___  \\
    /          |  |  |      |\ | |  ` |  ` __ |   / |  | |  /   /   |
   /          |   |   |     | \| |    |       |  /  |  | | /   /    |
  /           |   |   |     `  ' `--' `--'    ' '   `--' '    '     |
 /     ==<===|====|====|========== U.S.S. ENTERPRISE =============  |
<_-----------|---------|--------------------------------------------|
  \__         \       /             \      \            /        /  |
     `------_  \_____/_______________\______\__________/________/__/__
           / ||  ===   ==<============ NCC-1701/7 ======--------  ===/
           \_||___________________________________________________==/
                -===-                                             -===-
***********************************************************************

""")


def decor(foo):
    def wrap(text, state):
        print("*" * 71, "\n")
        foo(text, state)
        print()
        print("*" * 71)
    return wrap


@decor
def statement_output(text, state):
    if not state:
        print("GAME OVER")
        print()
        print(text)
    else:
        print(text)


txt = [
    "Welcome to the redshirt captain simulator!\n"
    "Your mission is to boldly go where no man has come before.\n"
    "You are on a Bridge, Captain.\n"
    "Where you go: to the captain's room, or to the turbolift?\n"
    "           Type: 'room' or 'lift' to go farther)",
    "You're the Captain!\n"
    "And beamimg down to the planet isn't Captain's work\n"
    "   for\n"
    "       all\n"
    "           safety!\n"
    "Clever choice, Captian. Goodday!",
    "You enter the turbolift and decide what will your order:\n"
    "Will you go to the transportator or to the hangar?\n"
    "           Type: 'beam' or 'hangar' to go farther",
    "You take a place on a plate, and order: 'Energize!'...\n"
    "You lost your breath in the endless sea of tribbles",
    "Yes! Hangar is the captain's choice. Comfortable and quiet\n"
    "You landed on the planet far from the sea of tribbles\n"
    "However, when you step outside, you hear, smell and...\n"
    "See thousands of Klingons running on you\n"
    "           Type: 'fight' or 'flight",
    "So... do you like the bloodwine on your lips?\n"
    "klingons joy of your fighting skills\n"
    "You can take one tribble as a trophey for your daughter",
    "Shame on you, Captain!\n"
    "   Shame\n"
    "       on you!\n"
    "How could you even pass the 'Kabayasi Maru test!'\n"
    "Klingons begins the war against your civilization!\n"
    "...\n"
    "...You wake up in your chair in captain's room...\n"
    "Phew, that was the only nightmare...",
    ]
choice = True

decor(statement_output(txt[0], choice))

answer = input("Your type: ").lower()

if answer == 'room':
    choice = False
    decor(statement_output(txt[1], choice))
    in_game = False
elif answer == 'lift':
    choice = True
    decor(statement_output(txt[2], choice))

if choice:
    answer = input("Your type: ").lower()

if answer == "beam":
    choice = False
    decor(statement_output(txt[3], choice))
    in_game = False
elif answer == 'hangar':
    choice = True
    decor(statement_output(txt[4], choice))

if choice:
    answer = input("Your type: ").lower()

if answer == "fight":
    choice = False
    decor(statement_output(txt[5], choice))
    in_game = False
elif answer == 'flight':
    choice = False
    decor(statement_output(txt[6], choice))
    in_game = False
else:
    choice = True
    decor(statement_output("You're not the Kirk!", choice))


quit()
