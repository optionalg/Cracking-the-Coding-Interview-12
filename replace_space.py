# Write a method to replace all spaces in a string with ‘%20’.

# input : string
# output: string
# working: iterate and for each space replace it with '%20'

def replace_space(string):
    res = ''
    for letter in string:
        if letter == ' ':
            res += '%20'
        else:
            res += letter
    return res

string = 'my name is sheela'
print (replace_space(string))