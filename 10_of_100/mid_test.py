def format_name(first, last):
    return (first + " " + last).title()


f_name = "des"
l_name = "kitten"
print(format_name(f_name, l_name))

def format_2(first, last):
    if first == "" or last == '':
        return "Fail!"
    return f"{first.title()} {last.title()}"


