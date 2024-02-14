h3 = {'S': 7,
      'A': 5,
      'B': 5,
      'C': 3,
      'G': 0
    }

class GRAPH:
    def __init__(self):
        self.graph_dict = {}

    def add_node(self, node):
        if node not in self.graph_dict:
            self.graph_dict[node] = {}

    def add_edge(self, node1, node2, weight):
        self.add_node(node1)
        self.add_node(node2)
        self.graph_dict[node1][node2] = weight
        self.graph_dict[node2][node1] = weight  # Assuming an undirected graph

    def reheap_up(self, heap, item): #this is reheap up up
        heap.append(item)
        current_index = len(heap) - 1
        while current_index > 0 and heap[current_index] < heap[(current_index - 1) // 2]:
            heap[current_index], heap[(current_index - 1) // 2] = heap[(current_index - 1) // 2], heap[current_index]
            current_index = (current_index - 1) // 2

    def reheap_down(self, heap): #this is reheap down
        
        print("Now in reheap_donwn: ", heap[0][0],heap[0][1],heap[0][2], h3[heap[0][1]])

        if not heap:
            return None
        if len(heap) == 1:
            return heap.pop()
        root = heap[0]
        heap[0] = heap.pop()
        i = 0
        while True:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            smallest = i
            if left_child < len(heap) and heap[left_child] < heap[smallest]:
                smallest = left_child
            if right_child < len(heap) and heap[right_child] < heap[smallest]:
                smallest = right_child
            if smallest != i:
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest
            else:
                break
        return root

    def ucs(self, start, goal):
        priority_queue = [(0, start, None)]
        visited = set()
        parent = {}

        while priority_queue:
            current_cost, current_node, current_parent = self.reheap_down(priority_queue)

            if current_node == goal:
                # Reconstruct and return the shortest path
                path = [current_node]
                while current_parent:
                    path.append(current_parent)
                    current_parent = parent.get(current_parent)
                path.reverse()
                return current_cost, path

            if current_node not in visited:
                visited.add(current_node)
                parent[current_node] = current_parent

                for neighbor, cost in self.graph_dict.get(current_node, {}).items():
                    if neighbor not in visited:
                        self.reheap_up(priority_queue, (current_cost + cost, neighbor, current_node))

        return float('inf'), []  # If goal is not reachable




graph = GRAPH()    
graph.add_node('S')
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('G')
graph.add_edge('C','G',3)
graph.add_edge('B','C',2)
graph.add_edge('B','G',6)
graph.add_edge('A','B',1)
graph.add_edge('A','C',4)
graph.add_edge('S','A',2)
graph.add_edge('S','B',4)

print(graph.ucs('S','G'))