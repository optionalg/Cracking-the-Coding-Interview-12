# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


lis = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
        [13,14,15,16]]

def rotate_matrix(lis):
    for layer in range(len(lis) // 2): # since we are swapping items so we only need to do for half the rows
        first_considered = layer
        last_considered = len(lis) - 1 - layer
        # we swap value firstly the four values at the corner, then the four values at second corners and so on.
        for index in range(0, last_considered - first_considered):
            offset = index - first_considered
            # save the top lefts value
            top = lis[first_considered][index + first_considered]
            # swap the value of top_left with bottom_left
            lis[first_considered][first_considered + index] = lis[last_considered - index][first_considered]
            # lis[first_considered][index] = lis[last_considered - offset][first_considered]
            # print (lis)
            # swap the value of bottom_left with bottom_right
            lis[last_considered - index][first_considered] = lis[last_considered][last_considered - index]
            # lis[last_considered - offset][first_considered] = lis[last_considered][last_considered - offset]
            # print (lis)
            # swap the value of the bottom_right with top_right
            lis[last_considered][last_considered - index] = lis[index + first_considered][last_considered]
            # lis[last_considered][last_considered - offset] = lis[index][last_considered]
            # print (lis)
            # swap the value of the top_right with the value stored in top
            lis[index + first_considered][last_considered] = top
            # print (lis)

print (lis)
rotate_matrix(lis)
print (lis)