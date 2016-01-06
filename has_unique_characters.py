# implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# with additional data structures
def unique_char(string):
    dic = {}
    for letter in string:
        if letter in dic:
            return False
        dic[letter] = 1
    return True

def has_unique_char(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True

string = 'sauron'
# print(has_unique_char(string))

# working: we assume that we are taking a number which is represented by 32 bits and we assume that thi number i.e checker initializes with all numbers occurance as False

def has_unique_character(string):
    string = string.lower()
    checker = 0 # 000000001...000
    for letter in string:
        number_form = ord(letter) - ord('a')
        bit_form_letter = 1 << number_form
        if (checker & bit_form_letter) > 0:
            return False
        checker = checker | bit_form_letter
    return True

print (has_unique_character(string))