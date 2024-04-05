class GRAPH:
    def __init__(self):
        self.graph = {}
    
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}
            print("Node added: ", node, "graph: ", self.graph)
        else:
            print("Node already exists: ", node, "graph: ", self.graph)

    def add_edge(self, source_node, target_node, weight):
        self.add_node(source_node)
        self.add_node(target_node)
        self.graph[source_node][target_node] = weight
        self.graph[target_node][source_node] = weight
        print("Edge added: ", source_node, " - ", target_node, " with weight: ", weight, "graph: ", self.graph)
    
    def reheapup(self, heap):
        current_index = len(heap) - 1
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if heap[current_index][0] < heap[parent_index][0]:
                #swap
                heap[current_index], heap[parent_index] = heap[parent_index], heap[current_index]
            else:
                #nouthing to swap
                break
            current_index = parent_index
            
    def reheapdown(self, heap):
        current_index = 0
        left_child_index = 2 * current_index + 1
        right_child_index = 2 * current_index + 2

        small = 0
        while(True):
            if left_child_index < len(heap) and heap[left_child_index] < heap[small]:
                small = left_child_index
            
            if right_child_index < len(heap) and heap[right_child_index] < heap[small]:
                small = right_child_index

            if small != current_index:
                #swap
                heap[current_index], heap[small] = heap[small], heap[current_index]
                current_index = small
            
            else: 
                break

    def popp(self, heap):
        if len(heap) == 0:
            #The heap is empty
            return None
        if len(heap) == 1:
            #The heap has only one item
            return heap.pop()
        
        root = heap[0]
        heap[0] = heap.pop()
        self.reheapdown(heap)
        return root

    def push(self, heap, item):
        heap.append(item)
        self.reheapup(heap)      

    def ucs(self, start, end):
            pqueue = [(0, start)]
            visited = set()
            while(pqueue):
                print("In the loop of pqueue", pqueue)
                current_cost, current_node = self.popp(pqueue)
                if current_node == end:
                    return current_cost
                if current_node in visited:
                    print("Node already visited: ", current_node, " with cost: ", current_cost, "visited set:", visited)
                    continue
                #else it will come
                if current_node not in visited:
                    print("Visiting node: ", current_node, " with cost: ", current_cost)
                    visited.add(current_node)
                    for neighbor, weight in self.graph[current_node].items():
                        if neighbor not in visited:
                            self.push(pqueue, (current_cost + weight, neighbor))



weighted_graph = GRAPH()
       # Add nodes
weighted_graph.add_node('A')
weighted_graph.add_node('B')
weighted_graph.add_node('C')
weighted_graph.add_node('D')
weighted_graph.add_node('E')
weighted_graph.add_node('F')


    # Add edges with weights
weighted_graph.add_edge('A', 'B', 3)
weighted_graph.add_edge('A', 'C', 2)
weighted_graph.add_edge('B', 'D', 1)
weighted_graph.add_edge('C', 'D', 4)
weighted_graph.add_edge('B', 'E', 5)
weighted_graph.add_edge('D', 'F', 4)
weighted_graph.add_edge('E', 'F', 2)

    # Perform UCS
start_node = 'A'
goal_node = 'F'
result = weighted_graph.ucs(start_node, goal_node)
print(result)