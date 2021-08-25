ENEMIES = 1  # Global var


def increase_enemies():
    enemies = 2  # new Local var
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {ENEMIES}")
# 2
# 1

# Python hasn't Block Scope
game_lvl = 3
en = ["Skeleton", "Zombie", "Alien"]
if game_lvl < 5:
    new_en = en[0]

print(new_en)

# but
def create_en():
    en = ["Skeleton", "Zombie", "Alien"]
    if game_lvl < 5:
        new_en = en[1]
    return new_en


print(new_en)
# Skeleton, not a Zombie

# Worse way, because it changes global vars and may cause the bugs
enemies = 1  # Global var


def increase_enemies():
    global enemies  # Call the global var like import from the same source
    enemies += 1  # Local var
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
# 2
# 2

# Better way
enemies = 1  # Global var


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
# 1
# 2

# Global constants
PI = 3.14159
URL = "http:"
