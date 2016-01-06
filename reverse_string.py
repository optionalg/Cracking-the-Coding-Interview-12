# Write code to reverse a C-Style String. (C-String means that “abcd” is represented as five characters, including the null character.)

def reverse_string(string):
    accumulator = ''
    for letter in string:
        accumulator = letter + accumulator
    return accumulator

string = "samman"
print (reverse_string(string))

def reverse_string_recursion(string):
    if len(string) < 1:
        return
    if len(string) == 1:
        return string
    return string[-1] + reverse_string_recursion(string[:-1])

print (reverse_string_recursion(string))