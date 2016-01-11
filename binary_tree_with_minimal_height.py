# Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.
lis = [2,3,4,5,6,7,8,10]

class NodeType(object):
    def __init__(self, data=None):
        self.data = data
        self.l_ptr = None
        self.r_ptr = None

tree = BinaryTree()

def create_tree(lis, start, end):
    if end < start:
        return
    mid = (end + start) // 2
    new_node = NodeType(lis[mid])
    new_node.lptr = create_tree(lis, start, mid - 1)
    new_node.rptr = create_tree(lis, mid + 1, end)
    return new_node

def main():
    return create_tree(lis, 0, len(lis) - 1)