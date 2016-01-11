# Write a program to sort a stack in ascending order. You should not make any assumptions about how the stack is implemented. The following are the only functions that should be used to write this program: push | pop | peek | isEmpty.
class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return not bool(len(self.stack))

def sort_stack(stack):
    res_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        if res_stack.is_empty():
            res_stack.push(temp)
        else:
            while res_stack.peek() < temp:
                temp1 = res_stack.pop()
                stack.push(temp1)
            res_stack.push(temp)
    return res_stack

a = Stack()
lis = [3,5,2,6,21, 22]
for i in lis:
    a.push(i) # 3,5,
a = sort_stack(a)
while not a.is_empty():
    print(a.pop(), end=' ')