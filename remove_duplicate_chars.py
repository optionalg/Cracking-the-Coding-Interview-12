# Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. NOTE: One or two additional variables are fine. An extra copy of the array is not. FOLLOW UP Write the test cases for this method.

# Since strings are immutable in python, so I shall do what the above question asks to a list

# For string:
string = "sssaaauron"
# output: "sauron"
string2 = "saruman"
# output : "sarumn"

# working1 : put them in a dictionary/set/list and see if an item is already in the dictionary, if not then add to the dictionary else remove from the final string

def remove_duplicates_string(string):
    letters = set()
    res = ''
    for letter in string:
        if letter in letters:
            continue
        letters.add(letter)
        res += letter
    return res

print (remove_duplicates_string(string2))

# working2: if order does not matter
def remove_duplicate(string):
    return ''.join(set(string))

print (remove_duplicate(string2))

# working 2: what we can do is we can use the find function to see if a character from the given string is in our result string. And if it is in our result string then we can skip it, or else we concatanate the character to the result

def remove_duplicates(lis):
    result_string = ''
    a = ''
    b = ''
    for character in lis:
        if not character in result_string:
            result_string = result_string + character
    return result_string

sa = 'samman'
print (remove_duplicates(sa))