class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def add_vertex(self, ver):
        self.vertex = Vertex(ver)
        self.adj_list[self.vertex.value] = []
        
    def add_child(self, parent, child, cost):
        self.edge = Edge(parent, child, cost)
        self.adj_list[parent].append((self.edge.child,self.edge.cost))

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, parent, child, cost):
        self.parent = parent
        self.child = child
        self.cost = cost

g = Graph()
g.add_vertex('S')
g.add_child('S','A',2)
g.add_child('S','B',4)

g.add_vertex('A')
g.add_child('A','B',1)
g.add_child('A','C',4)

g.add_vertex('B')
g.add_child('B','C',2)
g.add_child('B','G',6)

g.add_vertex('C')
g.add_child('C','G',3)


g.add_vertex('G')

class Minheap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0
        print("Minheap created: ", self.array)

    def getLeftChildIndex(self, index):
        return 2*(index) + 1
    
    def getRightChildIndex(self, index):
        return 2*(index) + 2
    
    def getParentIndex(self, index):
        return (index-1)//2
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def Parent(self, index):
        print("test 0", self.array[self.getParentIndex(index)][1][0], self.array)
        return self.array[self.getParentIndex(index)][1][0]+self.array[self.getParentIndex(index)][1][1]
    
    def LeftChild(self, index):
        return self.array[self.getLeftChildIndex(index)][1][0]+self.array[self.getLeftChildIndex(index)][1][1]
    
    def RightChild(self, index):
        return self.array[self.getRightChildIndex(index)][1][0]+self.array[self.getRightChildIndex(index)][1][1]
    
    def isFull(self):
        if len(self.array) == self.size:
            return True
        else:
            return False
        
    def isEmpty(self):
        if len(self.array) == 0:
            return True
        else: 
            return False
    
    def enqueue(self, data):
        if self.isFull():
            print("Full")
        
        else:
            self.array[self.size] = data
            self.size += 1
            self.reheapup()

    def reheapup(self):
        index = self.size - 1

        while(self.hasParent(index) and self.Parent(index) > self.array[index][1][0]+self.array[index][1][1]):
            self.array[self.getParentIndex(index)], self.array[index] = self.array[index], self.array[self.getParentIndex(index)]
            index = self.getParentIndex(index)

    def dequeue(self):
        if self.isEmpty():
            print("Empty")
        
        else:
            min = self.array[0]
            self.array[0] = self.array[self.size - 1]
            self.array[self.size-1] = None
            self.size -=1
            self.reheapdown()
            return min
        
    
    def reheapdown(self):
        index = 0

        while(self.hasLeftChild(index)):
            smallerChild = self.getLeftChildIndex(index)

            if(self.hasRightChild(index) and self.RightChild(index) < self.LeftChild(index)):
                smallerChild = self.getRightChildIndex(index)
            
            if self.array[smallerChild][1][0]+self.array[smallerChild][1][1] < self.array[index][1][0]+self.array[index][1][1]:
                self.array[smallerChild], self.array[index] = self.array[index], self.array[smallerChild]

                index = smallerChild

            else:
                break

def a_star(s,d):
    heuristic = {'S': 7,
                 'A': 5,
                 'B': 5,
                 'C': 3,
                 'G': 0}
   
    pq = Minheap(10)
    pq.enqueue(([s],[0,heuristic[s]]))
    while not pq.isEmpty():
        pair = pq.dequeue()
        cost = pair[1][0]
        path = pair[0]
        node = path[-1]
        if node == d:
            return pair

        for neighbor in g.adj_list[node]:
            print("g.adj_list[node]: ", g.adj_list[node])
            new_path = list(path)
            new_path.append(neighbor[0])
            new_cost = neighbor[1] + cost
            pq.enqueue((new_path, [new_cost,heuristic[neighbor[0]]]))
            print(pq.array)

print(a_star('S','G'))