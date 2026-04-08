class Queue:
    def __init__(self):
        self.queue=[]

    def isempty(self):
        if self.queue==[]:
            return True
        else:
            return False

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            item = self.queue.pop(0)
            print(f"Popped - {item}")

    def display(self):
        if self.isempty():
            print("Underflow")
        else:
            print(self.queue)

    def peek(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print(self.queue[0])

q = Queue()
q.enqueue(22)
q.enqueue(67)
q.enqueue(37)
q.dequeue()
q.peek()
q.display()