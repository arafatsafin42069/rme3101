import time

delay = 1


class MaxHeapPriorityQueue:
    def __init__(self):
        self.heap = []
    
    def reheapup(self):

        if(len(self.heap) <= 1):
            return 1

        child_index = len(self.heap) - 1
        parent_index = (child_index - 1) // 2

        while(child_index > 0):
            parent_index = (child_index - 1) // 2

            time.sleep(delay)
            print(f"now in reheapup ci:{child_index} pi:{parent_index} ,{self.heap}")

            if(self.heap[child_index] > self.heap[parent_index]):
                #we need to swap them
                self.heap[child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[child_index]

            child_index = parent_index

    
    def reheapdown(self):
        if(index == None):
            index = len(self.heap)-1
        while index > 0:
            print("now in reheap up")
            parent_index = (index - 1)//2
            if self.heap[parent_index] < self.heap[index]:
                #swap them
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]

            index = parent_index

    def reheapdown(self):
        parent_index = 0

        while True:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            time.sleep(1)
            print(f"now in reheapdown lci:{left_child_index} rci:{right_child_index} pi:{parent_index},{self.heap}")

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
        if len(self.heap) > 1:
            root = self.heap[0]
            self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
            self.heap.pop()
            self.reheapdown()
            
        else:
            self.heap.pop

        print(self.heap)
        

queue = MaxHeapPriorityQueue()
queue.enqueue(4)
queue.enqueue(12)
queue.enqueue(88)
queue.enqueue(9)
queue.enqueue(43)
queue.enqueue(25)
queue.enqueue(77)
queue.enqueue(61)
queue.enqueue(70)
queue.enqueue(31)
queue.enqueue(33)
queue.dequeue()
queue.dequeue()
queue.dequeue()



