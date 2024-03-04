import math
import json
import time
delay = 2

def minimax(input_graph, current_level, current_node, terminal_state, state, alpha, beta):
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
            value = max(value, minimax(input_graph, current_level+1, child, terminal_state, False, alpha, beta))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        print("current_level: ", current_level, "current_node: ", current_node, "return_value", value)
        return value


    if state == False:
        print("taking min from children", "current_node", current_node) 
        value = float('inf')
        for child in input_graph[current_node]:
            value = min(value, minimax(input_graph, current_level+1, child, terminal_state, True, alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                break
        print("current_level: ", current_level, "current_node: ", current_node, "return_value", value)
        return value

with open("C:\\Users\\Acer\\OneDrive\\Desktop\\3111\\Practice\\minmax.txt",'r') as f:
    input_list = []
    for line in f:
        dict = json.loads(line)
        input_list.append(dict)

print("input_list: ", input_list)

input_graph = input_list[0]
first_key = next(iter(input_graph))
terminal_state = input_list[1]


input_graph = { "A" : ["B","C"] ,
        "B" : ["D","E"] ,
        "C" : ["F","G"],
        "D" : ["H","I"],
        "E" : ["J","K"],
        "F" : ["L","M"],
        "G" : ["N","O"],
        "H" : ["P","Q"],
        "I" : ["R","S"],
        "J" : ["T","U"],
        "K" : ["V","W"],
        "L" : ["X","Y"],
        "M" : ["Z","a"],
        "N" : ["b","c"],
        "O" : ["d","e"],
        "P" : [],
        "Q" : [],
        "R" : [],
        "S" : [],
        "T" : [],
        "U" : [],
        "V" : [],
        "W" : [],
        "X" : [],
        "Y" : [],
        "Z" : [],
        "a" : [],
        "b" : [],
        "c" : [],
        "d" : [],
        "e" : [] }

terminal_state = val = {"P": 3, "Q": 4, "R" : 2, "S": 1, "T": 7, "U": 8, "V":9, "W":10, "X":2, "Y":11, "Z":1, "a":12, "b":14, "c":9, "d":13, "e":16}
first_key = "A"

print("graph: ", input_graph,"terminal_state: ", terminal_state)

#minimax(tree, '0',0, True, int(tree_height))
alpha = -float('inf')
beta = float('inf')
print(minimax(input_graph, 0 , first_key, terminal_state, True, alpha , beta ))