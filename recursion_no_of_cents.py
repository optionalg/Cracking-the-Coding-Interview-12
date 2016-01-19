# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of representing n cents.

# input -> number (cents), coin = 25
# output -> number of ways

# working ->
# get how many times the max can divide the number
# create that many paths: e.g with 1 25, 2 25, 3, 25, 0 25
# count these number of paths

def make_changes(num, max_det):
    if max_det == 25:
        next_det = 10
    elif max_det == 10:
        next_det = 5
    elif max_det == 5:
        next_det = 1
    elif max_det == 1:
        return 1 # base case as if we have a one now, then we can ust go on down until we get 0.
    no_itr = num // max_det
    count = 0
    # we start from 0 because one possible path is when you don’t take the max_det
    for i in range(0, no_itr + 1):
        count += make_changes(num - ( i * max_det), next_det)
    return count    

def change(cents):
    return make_changes(cents, 25)
        
    
print (change(10))


# test_cases -> 
# it can be 0
# it can be negative
# it can be an odd number
# it can be an even number
# it can be a very large number
# it can be decimal
# it can 1025
