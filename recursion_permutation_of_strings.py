def get_permutation(string, prefix, n, lis):
    if len(prefix) == n:
        lis.append(prefix)
    for i in range(len(string)):
        get_permutation(string[:i]+string[i+1:], prefix + string[i], n, lis)
    return lis

# a = get_permutation('saur', '', len('saur'), [])
# print(a, len(a))

# The way from the book 
# input -> a string
# output -> list of strings

def perm(string):
    # base case: when string is just one character long
    if len(string) == 0:
        return
    if len(string) == 1:
        return [string]
    # chop off the first character
    first = string[0]
    # get a list of permutation from the rest of the string
    rest_permu = perm(string[1:])
    # place the first character in all the possible places and get a list of the result
    res = put_in_all_positions(first, rest_permu)
    return res

def put_in_all_positions(character, lis_of_strings):
    res = []
    for strings in lis_of_strings:
        for position in range(len(strings) + 1):
            new_str = strings[0:position] + character + strings[position:]
            res.append(new_str)
    return res

a = 'saur'
s = perm(a)
print (s, len(s))