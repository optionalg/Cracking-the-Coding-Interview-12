# Write a method to decide if two strings are anagrams or not.

def are_anagrams(string1, string2):
    dic1 = {}
    dic2 = {}
    if len(string1) == len(string2):
        for character in string1:
            if character in dic1:
                dic1[character] += 1
            dic1[character] = 1
        for character in string2:
            if character in dic2:
                dic2[character] += 1
            dic2[character] = 1
        for character in dic1:
            if character not in dic2:
                return False
            if not (dic1[character] == dic2[character]):
                return False
        return True
    return False

string1 = ""
string2 = ""
print(are_anagrams(string1, string2))