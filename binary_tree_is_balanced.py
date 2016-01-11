# Implement a function to check if a tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that no two leaf nodes differ in distance from the root by more than one.

# class NodeType(object):
#     def __init__(self, data=None):
#         self.data = data
#         self.l_ptr = None
#         self.r_ptr = None

def is_balanced(binary_tree):
    return not bool((max_height(binary_tree) - min_height(binary_tree)) <= 1)

def max_height(root):
    if root == None:
        return 0
    return 1 + max_height(root.r_ptr, root.l_ptr)

def min_height(root):
    if root == None:
        return 0
    return 1 + min_height(root.r_ptr, root.l_ptr)

