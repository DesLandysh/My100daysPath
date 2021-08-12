def clear():
    print("\n"*20)


#d = {"bug": "here is the bugs",
#     "foo": "foo for slap the bugs",
#     "loop": "cyclon"}

#print(d["bug"])

# adding
d["if"] = "tasty"
#print(d["if"])

# create a new
empty = {}

# clear all from dict
# d = {}

d["if"] = "new state"

#print(d["if"])

# loop through
#for key in d:
#    print(key)
#    print(d[key])


# Nesting
travel_log = {
    "France": {"cities_visited": ["Paris", "Little", "Dijon"], "total_visits": 12},
    "Germany": "Berlin",
}

d = ["a", "b", ["c", "c1", "c2"]]

my_nested_dict = {
    "I_know": {
        "PL": ["Python", "Cpp"],
        "OP": ["Vim", "Pycharm"],
    },
    "I_want_to_know": {
        "PL": ["JS", "Kotlin"],
        "OP": ["Vim", "Android_SDK"],
    },
}
my_nested_list = [{
    "I_know": {
        "PL": ["Python", "Cpp"],
        "OP": ["Vim", "Pycharm"],
    },
    "I_want_to_know": {
        "PL": ["JS", "Kotlin"],
        "OP": ["Vim", "Android_SDK"],
    },
}]
