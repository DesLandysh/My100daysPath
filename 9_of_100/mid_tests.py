def clear():
    print("\n"*100)


d = {"bug": "here is the bugs",
     "foo": "foo for slap the bugs",
     "loop": "cyclon"}

print(d["bug"])

# adding
d["if"] = "tasty"
print(d["if"])

# create a new
empty = {}

# clear all from dict
#d = {}

d["if"] = "new state"

print(d["if"])

#loop through
for key in d:
    print(key)
    print(d[key])
clear()
