class FIFOQueue:
    def __init__(self, reverse_show  = 0):
        self.reverse_show = reverse_show
        self.stack = []

    def enqueue(self,data):
        self.stack.append(data)
        self.display()

    def dequeue(self):
        if len(self.stack) == 0:
            print("Not Available Data")
            return 23
        
        self.stack = self.stack[1:]
        self.display()

    def display(self):
        if self.reverse_show == 0:
            print(self.stack)
        elif self.reverse_show == 1:
            print(self.stack.reverse)
    


# queue = FIFOQueue()
# queue.enqueue(89)
# queue.enqueue(36)
# queue.enqueue(91)
# queue.enqueue(25)
# queue.enqueue(86)
# queue.dequeue()
# queue.dequeue()
# queue.enqueue(45)
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()




class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

obj = MyCircularQueue(5)
obj.enqueue(56)
obj.printCQueue()
obj.enqueue(484)
obj.printCQueue()
obj.enqueue(64)
obj.printCQueue()
obj.enqueue(97)
obj.printCQueue()
obj.enqueue(184)
obj.printCQueue()
obj.dequeue()
obj.printCQueue()
obj.dequeue()
obj.printCQueue()
obj.enqueue(184)
obj.printCQueue()
