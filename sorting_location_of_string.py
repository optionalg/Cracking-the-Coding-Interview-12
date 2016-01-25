# Given a sorted array of strings which is interspersed with empty strings, write a method to find the location of a given string.
# Example: find 'ball' in ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''] will return 4
# Example: find 'ballcar' in ['at', '', '', '', '', 'ball', 'car', '', '', 'dad', '', ''] will return -1

a = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
# for i in range(len(a)):
#     if a[i] == 'ball':
#         print(i)
#         break
# O(n)
# print (sorted(a))

def find_location(lis, word):
    top = len(lis) - 1
    bottom = 0
    while top >= bottom:
        # make sure that there is something at the start
        while lis[bottom] == '' and bottom <= top:
            bottom += 1
        if bottom > top:
            return -1
        # There is something at the start
        mid = (top + bottom) // 2
        while lis[mid] == '':
            mid -= 1
        if lis[mid] == word:
            return mid
        elif lis[mid] > word:
            top = mid - 1
        elif lis[mid] < word:
            bottom = mid + 1
    return -1

print (find_location(a, 'ball'))