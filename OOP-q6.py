class Stack:
    
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if (len(self.stack) == 0):
            return False
        
        item = self.stack.pop()
        return item

    def print_stack(self):
        for item in self.stack:
            print(f'| {item} |')
        print('_____\n\n')


stack = Stack()

stack.push(4)
print('push 4')
stack.print_stack()

stack.push(3)
print('push 3')
stack.print_stack()

stack.push(2)
print('push 2')
stack.print_stack()

stack.pop()
print('pop')
stack.print_stack()

stack.push(8)
print('push 8')
stack.print_stack()