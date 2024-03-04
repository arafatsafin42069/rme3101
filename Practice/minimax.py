import math
import json
import time
delay = 2

def minimax(input_graph, current_level, current_node, terminal_state, state):
    time.sleep(delay)

    if len(input_graph[current_node]) == 0:
        print("terminal state reached")
        return_value = terminal_state[current_node]
        print("current_level: ", current_level, "current_node: ", current_node, "return_value", return_value)
        return return_value

    if state == True:
        print("taking max from children", "current_node", current_node)
        value = -float('inf')
        for child in input_graph[current_node]:
            value = max(value, minimax(input_graph, current_level+1, child, terminal_state, False))
        print("current_level: ", current_level, "current_node: ", current_node, "return_value", value, "depth: ")
        return value


    if state == False:
        print("taking min from children", "current_node", current_node) 
        value = float('inf')
        for child in input_graph[current_node]:
            value = min(value, minimax(input_graph, current_level+1, child, terminal_state, True))
        print("current_level: ", current_level, "current_node: ", current_node, "return_value", value, "depth: ")
        return value

with open("C:\\Users\\Acer\\OneDrive\\Desktop\\3111\\Practice\\minimax1.txt",'r') as f:
    input_list = []
    for line in f:
        dict = json.loads(line)
        input_list.append(dict)

print("input_list: ", input_list)

input_graph = input_list[0]
first_key = next(iter(input_graph))
terminal_state = input_list[1]




print("graph: ", input_graph,"terminal_state: ", terminal_state, "tree_height: ", tree_height)

#minimax(tree, '0',0, True, int(tree_height))
print(minimax(input_graph, 0, first_key, terminal_state, True))