# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).


# input -> s1 and s2
# output -> boolean
# working ->
# if they have the same length and if s2 is a substring of s1 + s1 then s2 is a substring of s1

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s3 = s1 + s1
    return isSubstring(s3,s2)