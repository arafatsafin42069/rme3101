class Stack:

    last_index = 0

    def __init__(self, size = 10):
        self.size = size
        self.stack = []
        for i in range(size):
            self.stack.append(None)

        print("Stack Created ", self.stack)


    def enqueue(self, data):
        if self.last_index >= self.size :
            print("Not Enough Space")
            return 1
        
        self.stack.insert(self.last_index, data)
        self.last_index = self.last_index + 1
        print("Enqueued ", self.stack)
        

    def dequeue(self):
        if self.last_index == 0:
            print("Not Available Data")
            return 1

        self.stack[self.last_index - 1] = None
        self.last_index = self.last_index - 1
        print("Dequeued", self.stack)


stack = Stack(10)