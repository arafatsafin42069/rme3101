class PlainQueue:
    def __init__(self, size):
        self.size = size
        self.queue = []
        for i in range(0, self.size):
            self.queue.append(None)
        print(self.queue)
        self.front = self.rear = -1

    def enqueue(self, data):
        
        if self.rear == -1:
            self.rear = 0
            self.front = 0
            self.queue[self.rear] = data
            print(self.queue)
        elif self.front > self.rear:
            self.rear = 0
            self.front = 0
            self.queue[self.rear] = data
            print(self.queue)
        elif self.rear < self.size - 1:
            self.rear = self.rear + 1
            self.queue[self.rear] = data
            print(self.queue)
        else:
            print("Not enough space")
            print("now in enqueue front: ", self.front, "rear", self.rear, "\n")
            return 1
        print("now in enqueue front: ", self.front, "rear", self.rear, "\n")
    
    def dequeue(self):
        

        if(self.front > self.rear):
            print("Not enouth Data")
            print("in the dequeue", "front: ", self.front, "rear", self.rear, "\n")
            return 1
        
        self.queue[self.front] = None
        self.front = self.front + 1
        print(self.queue)
        print("in the dequeue", "front: ", self.front, "rear", self.rear, "\n")

queue = PlainQueue(10)
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")
queue.enqueue("d")
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")
queue.enqueue("d")
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")
queue.enqueue("d")

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue("d")
queue.enqueue("d")
queue.dequeue()
queue.enqueue("d")

