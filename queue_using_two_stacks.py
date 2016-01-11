# Implement a MyQueue class which implements a queue using two stacks.

class Queue(object):
    def __init__(self, stack1, stack2):
        self.stack1 = stack1
        self.stack2 = stack2

    def enqueue(self, item):
        self.stack1.push(item)
        # self.pop_and_push(self.stack2, self.stack1)
        # self.stack1.push(item)
        # self.pop_and_push(self.stack1, self.stack2)

    def pop_and_push(self, stack1, stack2):
        while not stack1.is_empty():
            obj = stack1.pop()
            stack2.push(obj)

    def dequeue(self):
        if self.stack2.is_empty():
            if self.stack1.is_empty():
                return None
            self.pop_and_push(self.stack1, self.stack2)
            return self.stack2.pop()
        return self.stack2.pop()
        # return self.stack2.pop()


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return not bool(len(self.stack))

s1 = Stack()
s2 = Stack()

a = Queue(s1, s2)
lis = [3,5,2,6,21,67,4]
for i in lis[:4]:
    a.enqueue(i)
print(a.dequeue())
print (a.dequeue())
for i in lis[4:]:
    a.enqueue(i)
for i in range(3):
    print(a.dequeue())
print(a.dequeue())
a.enqueue(81)
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())