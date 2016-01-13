# Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth (i.e., if you have a tree with depth D, you’ll have D linked lists).
# input -> binary search tree
# output -> list of linked list heads

# working: we do a breadth first traversal and we have a value that will indicate which level we should be in

def level_linked_lists(root):
    traversal_queue = Queue()
    traversal_queue.enqueue(root)
    items_in_linked_list = 0
    max_for_current_level = 1
    current_level = 0
    res = []
    while not traversal_queue.is_empty():
        item = traversal_queue.dequeue()
        traversal_queue.enqueue(item.left_child)
        traversal_queue.enqueue(item.right_child)
        if len(res) == 0:
            node = NodeType(item)
            res.append(node)
            items_in_linked_list = 1
        elif items_in_linked_list == max_for_current_level:
            current_level += 1
            max_for_current_level = 2 ** (current_level)
            node = NodeType(item)
            res.append(node)
            items_in_linked_list = 1
        else:
            node.next = NodeType(item)
            node = node.next