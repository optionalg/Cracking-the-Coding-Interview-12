# Write a method to sort an array of strings so that all the anagrams are next to each
# other.

# # input -> array of strings
#     are the strings ordered lexicographically? -> Not
#     are they very long strings? -> short strings? from 0 to about 10 letters long
#     they can be empty strings, handle this
#     One character long string
    
# # output: return an array
#     Do you have any restriction in the space complexity of the solution. 
#     from our array -> [3,5,6,3]
# append the chosen to our list -> append all possible anagrams for that string and remove them from the original list
#     this will have a space complexity of O(n) and time complexity of O(n^2).
                    
# Working:
# Does the order matter?
# If not then we can use a dictionary, and store the keys as a lexicographically sorted group of letter and the values as all the permutation in our list of words that forms from it.

def get_sorted_string(string):
    return ''.join(sorted(string))

def arrange_by_anagram(strings):
    anagrams = {}
    res_lis = []
    for string in strings:
        sorted_string = get_sorted_string(string)
        if sorted_string not in anagrams:
            anagrams[sorted_string] = []
        anagrams[sorted_string].append(string)
    for k in anagrams:
        res_lis.extend(anagrams[k])
    return res_lis

lis = ['samman', 'sauron', 'nammas','uron','aammns', 'aurson']
print (arrange_by_anagram(lis))