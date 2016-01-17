# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


lis = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
        [13,14,15,16]]

def rotate_matrix(lis, by):
    if by == 90:
        times = 1
    elif by == 180:
        times = 2
    elif by == 270:
        times = 3
    elif times == 360:
        times = 0
    for rotate in range(times):
        for layer in range(len(lis) // 2): # since we are swapping items so we only need to do for half the rows
            first = layer
            last = len(lis) - 1 - layer
            # we swap value firstly the four values at the corner, then the four values at second corners and so on.
            for i in range(first, last):
                offset = i - first
                # save the top lefts value
                top = lis[first][i]
                # swap the value of top_left with bottom_left
                lis[first][i] = lis[last - offset][first]
                # swap the value of bottom_left with bottom_right
                lis[last - offset][first] = lis[last][last - offset]
                # swap the value of the bottom_right with top_right
                lis[last][last - offset] = lis[first + offset][last]
                # swap the value of the top_right with the value stored in top
                lis[first + offset][last] = top
                # print (lis)
    print (lis)

print (lis)
rotate_matrix(lis, 180)