import file_to_graph1

cutted_node = []
traverse_node = []

def minimax(input_graph, current_node, final_node_value, state, alpha, beta):

    if len(input_graph[current_node]) == 0:
        traverse_node.append(current_node)
        print("this is final state: ", final_node_value[current_node])
        return final_node_value[current_node]
    
    if state == True:
        #we will find maximum here
        v = -float('inf')
        for child in input_graph[current_node]:
            traverse_node.append(current_node)
            v = max(v, minimax(input_graph, child, final_node_value, False, alpha, beta))
            alpha =  max(alpha, v)
            if beta <= alpha:
                cutted_node.append(current_node)
                break
        return v
    
    if state == False:
        #here we will find minimum
        v = float("inf")
        for child in input_graph[current_node]:
            traverse_node.append(current_node)
            v = min(v, minimax(input_graph, child, final_node_value, True, alpha, beta))
            beta = min(beta, v)
            if beta <= alpha:
                cutted_node.append(current_node)
                break
        return v
    
input_graph, terminal_state_value, all_node = file_to_graph1.file_to_graph("C:\\Users\\Acer\\OneDrive\\Desktop\\3111\\L8 Alpha Beta\\input_text2.txt")
v = minimax(input_graph, "A", terminal_state_value, True, float("-inf"), float("inf"))
print(v)
print("path_followed: ",traverse_node)
print("cutted_node: ",cutted_node)

pruned_node = []
for node in all_node:
    if node not in traverse_node:
        pruned_node.append(node)


final_answer_node = ""
for key, value in terminal_state_value.items():
    if value == v:
        final_answer_node = key
        break
print("final_answer_node: ", final_answer_node)

optimal_path = [final_answer_node]
while True:
    for key, value in input_graph.items():
        if optimal_path[-1] in value:
            optimal_path.append(key)
            break
    if key == "A":
        break   

print("optimal_path(reverse): ", optimal_path)
optimal_path.reverse()
print("optimal_path: ", optimal_path)


print("pruned_node: ", pruned_node)
