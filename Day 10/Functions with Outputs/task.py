# def format_name(name, surname):
#     name = name.title()
#     surname = surname.title()
#
#     print(f"{name} {surname}")
#
# format_name("kerem", "dogan"

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)