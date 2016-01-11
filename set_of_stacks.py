# Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks, and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

class SetOfStacks(object):
    def __init__(self, max_limit):
        self.max_limit = max_limit
        self.current_stack_amount = 0
        self.current_stack_index = 0
        self.set_of_stack = []

    def is_empty(self):
        return not bool(len(self.set_of_stack))

    def push(self, item):
        if self.is_empty():
            new_stack = Stack()
            self.set_of_stack.append(new_stack)
            self.current_stack_index = 0
            self.set_of_stack[self.current_stack_index].push(item)
            self.current_stack_amount = 1
        elif self.current_stack_amount < self.max_limit:
            self.set_of_stack[self.current_stack_index].push(item)
            self.current_stack_amount += 1
        elif self.current_stack_amount == self.max_limit:
            new_stack = Stack()
            self.set_of_stack.append(new_stack)
            self.current_stack_index += 1
            print(self.current_stack_index, '<<<, pushing')
            self.set_of_stack[self.current_stack_index].push(item)
            self.current_stack_amount = 0

    def pop(self):
        if not self.is_empty():
            if self.current_stack_amount == -1:
                self.set_of_stack.pop()
                self.current_stack_amount = self.max_limit - 1
                self.current_stack_index -= 1
            self.current_stack_amount -= 1
            item = self.set_of_stack[self.current_stack_index].pop()
            return item
        return None

a = SetOfStacks(5)

lis = [3,5,2,6,21, 22]
for i in lis:
    a.push(i) # 3,5,
print(a.pop())
print (a.pop())
for i in lis[4:]:
    a.push(i)
for i in range(3):
    print(a.pop())
print(a.pop())
a.push(81)
print(a.pop())
print(a.pop())
print(a.pop())