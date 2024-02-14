import os

def next_page_terminal(line = 10):
    for i in range(line):
        print("\n")
    


class Node:
    def __init__(self, node_name):
        self.node_name = node_name
        print("Node created: ", self.node_name)

class Edge:
    def __init__(self, parent, child, cost):
        self.parent = parent
        self.child = child
        self.cost = cost
        print("Edge created: ", self.parent, self.child, self.cost)

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_node(self, node):
        self.node = Node(node)
        self.graph[self.node.node_name] = []
        #so we will access like graph[current_node][(child_node, cost), (child_node1, cost1 )] 
    
    def add_edge(self, parent, child, cost):
        self.edge = Edge(parent, child, cost)
        self.graph[parent].append((self.edge.child, self.edge.cost))
        print("Edge added ", "Graph: ", self.graph)

class Minheap:
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
        return self.array[self.get_parent_index(index)][1][0] +  self.array[self.get_parent_index(index)][1][1]
        #we will add both the cost and the heuristic value
    def left_child_value(self, index):
        return self.array[self.get_left_child_index(index)][1][0] +  self.array[self.get_left_child_index(index)][1][1]
    def right_child_value(self, index):
        return self.array[self.get_right_child_index(index)][1][0] +  self.array[self.get_right_child_index(index)][1][1]
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
    def heapify_up(self):
        index = self.last_index - 1
        while self.has_parent(index) and self.parent_value(index) > self.array[index][1][0] + self.array[index][1][1]:
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
            print("Dequeue: ", self.array, "root: ", root)
            return root
    def heapify_down(self):
        if self.is_empty():
            print("Heap is empty nothing to heapify down")
        else:
            index = 0 
            while self.has_left_child(index):
                print("Heapify down: ", self.array, "current index: ", index)
                smaller_child_index = self.get_left_child_index(index) #assuming left child is smaller
                if self.has_right_child(index) and self.right_child_value(index) < self.left_child_value(index):
                    smaller_child_index = self.get_right_child_index(index)
                    #amra kintu right_child_value and left_child_value ber korar time e 
                    #heuristic value o add kore niyechi

                if self.array[smaller_child_index][1][0]+self.array[smaller_child_index][1][1] < self.array[index][1][0]+self.array[index][1][1]:
                    self.swap(smaller_child_index, index)

                    index = smaller_child_index
                
                else:
                    break

def a_star_func(graph, source,destination,heuristic):
    priority_queue = Minheap(size=10)
    priority_queue.enqueue((source, (0, heuristic[source])))


    while not priority_queue.is_empty():
        print("Priority queue: ", priority_queue.array)
        path_cost_heuristic = priority_queue.dequeue()
        path = path_cost_heuristic[0]
        cost = path_cost_heuristic[1][0]
        last_node = path[-1]

        if last_node == destination:
            return path_cost_heuristic
        
        for neighbor in graph.graph[last_node]:
            new_path = list(path)
            new_path.append(neighbor[0])
            new_cost = neighbor[1] + cost #this is the old cost + the new cost
            priority_queue.enqueue((new_path, (new_cost, heuristic[neighbor[0]])))
            #path, (cost, heuristic_of_the_neighbor)
            print(priority_queue.array)

def print_path(li):
    for i in li[:len(li)-1]:
        print(i, end = " > ")
    print(li[-1])
    print("\n")


    
graph = Graph()

graph.add_node("S")
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("G")
graph.add_edge('C','G',3)
graph.add_edge('B','C',2)
graph.add_edge('B','G',6)
graph.add_edge('A','B',1)
graph.add_edge('A','C',4)
graph.add_edge('S','A',2)
graph.add_edge('S','B',4)

final_result = a_star_func(graph, 'S', 'G', {'S': 7, 'A': 5, 'B': 5, 'C': 3, 'G': 0})

next_page_terminal(line = 10)
print_path(final_result[0])
print("Cost: ", final_result[1][0])

