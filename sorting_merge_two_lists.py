# Pythonic way -> costs a lot of space O(n ** 3)
def merge(lisA, lisB):
    if not lisA and not lisB:
        return
    if not lisA:
        return lisB
    if not lisB:
        return lisA
    if lisA[0] > lisB[0]:
        return [lisB[0]] + merge(lisA, lisB[1:])
    else:
        return [lisA[0]] + merge(lisA[1:], lisB)

lis1 = [3,4,5,66,77,88]
lis2 = [6,8,9,12,454,623]
# print (merge(lis1, lis2))

# Non-pythonic, and pointer oriented
def merge(lisA, lisB):
    j = len(lisB) - 1
    k = len(lisA) - 1
    i = k - j - 1
    while i >= 0 and j >= 0:
        # case 1 ->  
        if lisA[i] > lisB[j] : 
            lisA[k] = lisA[i]
            i -= 1
            k -= 1
        #case 2 -> 
        if lisB[j] >= lisA[i]: 
            lisA[k] = lisB[j]
            j -= 1
            k -= 1

    while j >= 0:
        lisA[k] = lisB[j]
        j -= 1
        k -= 1

lisa = [0,0]
lisb = [3]
merge(lisa, lisb)
print (lisa)
# test cases ->
# empty lists
# one empty one working - 2 cases
# both normal
# unsorted lists