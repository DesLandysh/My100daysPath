
dict_file = open("dict.txt", "r")
word_list = []
for line in dict_file:
    word_list.append(line[:-1])

dict_file.close()
