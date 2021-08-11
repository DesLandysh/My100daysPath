# blind bit program

def clear():
    print("\n"*20)


print("Welcome to the blind bit program")
blind_bit = {}
next_person = True
while next_person:
    name = input("Enter your name: ").capitalize()
    bit = int(input("What's your bit? $"))
    blind_bit[name] = bit
    if input("Is there another person to bit? yes/no :").lower() == "yes":
        clear()
    else:
        next_person = False

high = 0
winner = ""
for key in blind_bit:
    if high < blind_bit[key]:
        high = blind_bit[key]
        winner = key
    else:
        continue

clear()
print(f"\nAnd the winner is {winner} who bit ${high}.")
