class Stack:
    def __init__(self):
        self.stack=[]

    def isEmpty(self):
        return len(self.stack)==0

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if self.stack==[]:
            print("Stack is empty")
        else:
            item = self.stack.pop()
            print(f"Popped - {item}")
    def peek(self):
        if self.stack==[]:
           print("Stack is empty")
        else:
            print(self.stack[-1])

    def display(self):
        print(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.peek()
s.display()