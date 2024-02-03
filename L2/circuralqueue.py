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
        elif (self.rear + 1)%self.size == self.front:#The stack is full
            print("The stack is full")
            return 1
        else:
            self.rear = (self.rear + 1)%self.size
            self.queue[self.rear] = data

        print(self.queue," front: ", self.front, "rear", self.rear, "\n")
        
        pass
        
    def dequeue(self):
        self.queue[self.front] = None
        self.front = (self.front + 1)%self.size
        print(self.queue," front: ", self.front, "rear", self.rear, "\n")

        if(self.front == self.rear+1):
            self.front = -1
            self.rear = -1
            print("The queue will be restarted or there is not enough data")
        pass

    def showQ(self):
        print("\n\n","Result:        ", self.queue,"\n\n")

queue = PlainQueue(5)
queue.enqueue(14)
queue.enqueue(22)
queue.enqueue(13)
queue.enqueue(-6)
queue.showQ()


queue.dequeue()
queue.dequeue()
queue.showQ()

queue.enqueue(9)
queue.enqueue(20)
queue.enqueue(5)
queue.showQ()


queue.enqueue(20)





# queue = PlainQueue(10)
# queue.enqueue("a")
# queue.enqueue("b")
# queue.enqueue("c")
# queue.enqueue("d")
# queue.enqueue("a")
# queue.enqueue("b")
# queue.enqueue("c")
# queue.enqueue("d")
# queue.enqueue("a")
# queue.enqueue("b")
# queue.enqueue("c")
# queue.enqueue("d")


# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()

# queue.enqueue("c")
# queue.enqueue("d")
# queue.enqueue("c")
# queue.enqueue("d")
# queue.enqueue("h")
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()


# queue.dequeue()
# queue.dequeue()
# queue.dequeue()


# queue.enqueue("c")
# queue.enqueue("d")
# queue.enqueue("c")
# queue.enqueue("d")
# queue.enqueue("h")


# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()