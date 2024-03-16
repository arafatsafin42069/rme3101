import file_to_graph1

pruned_node = []
traverse_node = []

def minimax(input_graph, current_node, final_node_value, state, alpha, beta):

    if len(input_graph[current_node]) == 0:
        traverse_node.append(current_node)
        print("this is final state returning: ", final_node_value[current_node])
        return final_node_value[current_node]
    
    if state == True:
        #Find the max 
        v = -float('inf')
        for child in input_graph[current_node]:
            traverse_node.append(current_node)
            v = max(v, minimax(input_graph, child, final_node_value, False, alpha, beta))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v
    
    if state == False:
        #Find the min
        v = float('inf')
        for child in input_graph[current_node]:
            traverse_node.append(current_node)
            v = min(v, minimax(input_graph, child, final_node_value, True, alpha, beta))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v

input_graph, terminal_state_value = file_to_graph1.file_to_graph("C:\\Users\\Acer\\OneDrive\\Desktop\\3111\\L8 Alpha Beta\\input_text1.txt")

print(minimax(input_graph, "A", terminal_state_value, True, alpha = -float('inf'), beta = float('inf')))
print("path_followed: ",traverse_node)