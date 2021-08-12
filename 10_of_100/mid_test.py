def format_name(first, last):
    return (first + " " + last).title()


f_name = "des"
l_name = "kitten"
print(format_name(f_name, l_name))


def format_2(first, last):
    """
    Takes name's part and combine them into full proper name
    :param first: name
    :param last: surname
    :return: titled full name
    """
    if first == "" or last == '':
        return "Fail!"
    return f"{first.title()} {last.title()}"


print(format_2(f_name, l_name))
