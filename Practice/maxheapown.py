import time

class MaxHeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def reheapup(self, index = None):
        if(index == None):
            index = len(self.heap)-1
        while index > 0:
            print("now in reheap up")
            parent_index = (index - 1)//2
            if self.heap[parent_index] < self.heap[index]:
                #swap them
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]

            index = parent_index

    def reheapdown(self, index=0):
        parent_index = index

        while True:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            if left_child_index >= len(self.heap) and right_child_index >= len(self.heap):
                break

            max_child_index = parent_index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[max_child_index]:
                max_child_index = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[max_child_index]:
                max_child_index = right_child_index

            if max_child_index != parent_index:
                self.heap[max_child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[max_child_index]
                parent_index = max_child_index
            else:
                break


            





    
    def enqueue(self, data):
        self.heap.append(data)
        self.reheapup()
        print(self.heap)
    
    def dequeue(self):
        if not self.heap:
            return None
        
        root = self.heap[0]

        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self.reheapdown()
        else:
            self.heap.pop()
        print(self.heap)
    

priorityQueue = MaxHeapPriorityQueue()
priorityQueue.enqueue(10)
priorityQueue.enqueue(9)
priorityQueue.enqueue(8)
priorityQueue.enqueue(7)
priorityQueue.enqueue(6)
priorityQueue.enqueue(5)
priorityQueue.enqueue(4)
priorityQueue.enqueue(3)
priorityQueue.enqueue(2)

priorityQueue.dequeue()

