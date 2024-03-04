import os

class Minheap_a_star:
    def __init__(self, size = 20):
        self.size = size
        self.last_index = 0 #this will keep track of the last available index
        #if there is no element then it will be 0
        #if there is one element then it will be 1 (1 is index of second space)
        self.array = []
        for i in range(self.size):
            self.array.append(None)
        print("Minheap created: ", self.array)
    
    def get_parent_index(self, index):
        return (index-1)//2
    def get_left_child_index(self, index):
        return 2*index + 1
    def get_right_child_index(self, index):
        return 2*index + 2
    def has_parent(self, index):
        return self.get_parent_index(index) >= 0
    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.last_index
    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.last_index
    def parent_value(self, index):
        return self.array[self.get_parent_index(index)][1] +  self.array[self.get_parent_index(index)][2]
        #we will add both the cost and the heuristic value
    def left_child_value(self, index):
        return self.array[self.get_left_child_index(index)][1] +  self.array[self.get_left_child_index(index)][2]
    def right_child_value(self, index):
        return self.array[self.get_right_child_index(index)][1] +  self.array[self.get_right_child_index(index)][2]
    def is_full(self):
        return self.last_index == len(self.array)
    def is_empty(self):
        return self.last_index == 0
    def enqueue(self, value):
        if self.is_full():
            print("Heap is full current elements are: ", self.array)
        else: 
            self.array[self.last_index] = value #we have to add in the last position 
            self.last_index = self.last_index + 1
            self.heapify_up()
            print("Enqueueing: ", value, "current array: ", self.array)
    def heapify_up(self):
        index = self.last_index - 1
        while self.has_parent(index) and self.parent_value(index) > self.array[index][1] + self.array[index][2]:
            #if parent value is greater than the current value then swap
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)
            print("Heapify up: ", self.array, "current index: ", index, "parent index: ", self.get_parent_index(index))
    def swap(self, index1, index2):
        print("swapping: ", index1, index2, "array: ", self.array)
        temp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp
    def dequeue(self):
        if self.is_empty():
            print("Heap is empty nouthing to dequeue")
        else:
            root = self.array[0]
            self.array[0] = self.array[self.last_index - 1]
            self.array[self.last_index - 1] = None
            self.last_index = self.last_index - 1
            self.heapify_down()
            print("Dequeued ", root, " and array: ", self.array)
            return root
    def heapify_down(self):
        if self.is_empty():
            print("Heap is empty nothing to heapify down")
        else:
            index = 0 
            while self.has_left_child(index):
                smaller_child_index = self.get_left_child_index(index) #assuming left child is smaller
                if self.has_right_child(index) and self.right_child_value(index) < self.left_child_value(index):
                    smaller_child_index = self.get_right_child_index(index)
                    #amra kintu right_child_value and left_child_value ber korar time e 
                    #heuristic value o add kore niyechi
                if self.array[smaller_child_index][1]+self.array[smaller_child_index][2] < self.array[index][1]+self.array[index][2]:
                    self.swap(smaller_child_index, index)
                    index = smaller_child_index
                else:
                    break
                print("Heapify down: ", self.array, "current index: ", index)

def a_star(graph, start_node, target_node, h):
    os.system('cls')
    priority_queue = Minheap_a_star(size=10)
    priority_queue.enqueue([[start_node], 0, h[start_node]])
    #the cost will be path_list, g, h

    while not priority_queue.is_empty():
        poped_node = priority_queue.dequeue()
        path_followed = poped_node[0]
        cost = poped_node[1]
        current_node = path_followed[-1]

        print("popped node: ", poped_node, "current node: ", current_node, "cost: ", cost, "path: ", path_followed)

        if current_node == target_node:
            os.system('cls')
            return poped_node
        
        for child in graph[current_node]:
            #child is a tuple (next_node, cost to go there)
            print("child: ", child)
            next_node = child[0]
            new_path = []
            for node in path_followed:
                new_path.append(node)
            new_path.append(child[0])
            new_cost = cost + child[1]
            print("new path: ", new_path, "new cost: ", new_cost, "h: ", h[next_node])
            priority_queue.enqueue([new_path, new_cost, h[next_node]])



graph = {
    "S": [("A", 2), ("B", 4)],
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("G", 6)],
    "C": [("G", 3)]
}
h3 = {
    "S": 7,
    "A": 5,
    "B": 5,
    "C": 3,
    "G": 0
}


print(a_star(graph, "S", "G", h3))
