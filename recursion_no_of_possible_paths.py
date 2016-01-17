# Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can only move in two directions: right and down. How many possible paths are there for the robot?

# FOLLOW UP
# Imagine certain squares are “off limits”, such that the robot can not step on them. Design an algorithm to get all possible paths for the robot.

def possible_paths(grid, x_pos, y_pos):
    # test case handling:
    if x_pos > len(grid) - 1 or y_pos > len(grid) - 1:
        return -1

    # base case: when we cannot move, that is we are at the bottom right most cell
    if x_pos == len(grid) - 1 and y_pos == len(grid) - 1:
        return 0
 
    # case 1: when we have both directions to go to
    if x_pos < len(grid) - 1 and y_pos < len(grid) - 1:
        return 1 + possible_paths(grid, x_pos + 1, y_pos) + 1 + possible_paths(grid, x_pos, y_pos + 1)

    #case 2: when we can only move right
    if x_pos < len(grid) - 1:
        return 1 + possible_paths(grid, x_pos + 1, y_pos)
        
    # case 3: when we can only move down
    if y_pos < len(grid) - 1:
        return 1 + possible_paths(grid, x_pos, y_pos + 1)

lis = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

# Test cases:
# robot_pos = (3,1)
# robot_pos = (0,0)
# robot_pos = (2,2)
# robot_pos = (2,1)
# robot_pos = (2,3)

print (possible_paths(lis, robot_pos[0], robot_pos[1]))