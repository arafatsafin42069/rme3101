import json

def minimax(input_graph, current_node, final_node_value, state):

    if len(input_graph[current_node]) == 0:
        print("returning: ", final_node_value[current_node])
        return final_node_value[current_node]
    
    if state == True:
        #find the max() or return the max
        max_value = -float('inf')
        for child in input_graph[current_node]:
            print("comparing: ", max_value, minimax(input_graph, child, final_node_value, False), "current_node", child)
            max_value = max(max_value, minimax(input_graph, child, final_node_value, False))
        print("returning: ", max_value)
        return max_value
    
    if state == False:
        #find the max() or return the max
        min_value = float('inf')
        for child in input_graph[current_node]:
            print("comparing: ", min_value, minimax(input_graph, child, final_node_value, True), "current_node", child)
            min_value = min(min_value, minimax(input_graph, child, final_node_value, True))
        print("returning: ", min_value)
        return min_value
       
with open("C:\\Users\\Acer\\OneDrive\\Desktop\\3111\\Practice\\minimax\\minimax.txt", "r") as f:
    input_li = []
    for line in f:
        input_li.append(json.loads(line))   
    print(input_li[0],"\n", input_li[1])


# input_graph = input_li[0]
# final_node_value = input_li[1]


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

terminal_state =  {"P": 3, "Q": 4, "R" : 2, "S": 1, "T": 7, "U": 8, "V":9, "W":10, "X":2, "Y":11, "Z":1, "a":12, "b":14, "c":9, "d":13, "e":16}


print(minimax(input_graph, "A", terminal_state, True))