# In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (e.g., each disk sits on top of an even larger one). You have the following constraints: 
# (A) Only one disk can be moved at a time.
# (B) A disk is slid off the top of one rod onto the next rod.
# (C) A disk can only be placed on top of a larger disk.
#
# Write a program to move the disks from the first rod to the last using Stacks.
def hanoi(n, source, helper, target):
    if n > 0:
        # move the tower above n to the auxulary Stack
        hanoi(n - 1, source, target, helper)
        # move the nth disk form source to helper
        if source:
            target.append(source.pop())
        # move the n - 1 disks from helper to target
        hanoi(n - 1, helper, source, target)
        
source = [4,3,2,1, 9]
target = []
helper = []
hanoi(len(source),source,helper,target)

print (source, helper, target)