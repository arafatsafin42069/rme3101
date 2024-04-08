
import sys
import time

# neighbors = {
#     'WA' : ['NT', 'SA'],
#     'NT' : ['WA', 'SA', 'Q'],
#     'SA' : ['WA', 'NT', 'Q', 'NSW', 'V'],
#     'Q' :  ['NT', 'SA', 'NSW'],
#     'NSW' :  ['Q', 'SA','V'],
#     'V' :  ['NSW', 'SA'],
#     'T' :  ['']
# }

# colors = ['Red', 'Green', 'Blue']

# states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']





neighbors = {
    'A': ['B','D','E'],
    'B': ['A','E','F','C'],
    'C': ['B','F'],
    'D': ['A','E','G','H'],
    'E': ['A','B','D','F','H','I'],
    'F': ['B','C','E','I'],
    'G': ['D','H'],
    'H': ['D','E','G','I'],
    'I': ['E','F','H']
}
colors = ['Blue', 'Red', 'Green']
states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

# neighbors = {
#     'A': ['B', 'V'],
#     'B': ['A', 'V'],
#     'C': ['F', 'H', 'D'],
#     'D': ['G', 'H', 'C'],
#     'G': ['K', 'D'],
#     'F': ['K', 'C'],
#     'K': ['J', 'F', 'G', 'O'],
#     'J': ['K', 'N'],
#     'N': ['J'],
#     'H': ['V', 'C', 'D', 'M'],
#     'E': ['I'],
#     'I': ['E', 'M'],
#     'M': ['Q', 'H', 'I'],
#     'Q': ['M', 'L'],
#     'L': ['P', 'Q'],
#     'P': ['L', 'U', 'T', 'S'],
#     'U': ['T', 'P', 'a'],
#     'T': ['P', 'U', 'a', 'Z'],
#     'S': ['P', 'Z', 'Y', 'X', 'R'],
#     'R': ['W', 'X', 'S'],
#     'a': ['U', 'T', 'Z'],
#     'Z': ['a', 'T', 'S', 'Y'],
#     'Y': ['Z', 'S', 'X'],
#     'X': ['Y', 'S', 'R', 'W'],
#     'W': ['X', 'R', 'V'],
#     'V': ['A', 'B', 'H', 'W'],
#     'O': ['K']
# }
# states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a']
# colors = ['Blue', 'Red', 'Green']




states_where_made_decision_optional = {}
colors_of_states = {}


def check_valid_input():
    for state_key, state_value in neighbors.items():
        #print("State Key: ", state_key, " State Value: ", state_value)
        if state_key not in states:
            print("State dictionary and list are not matching")
            return False
        for neighbor in state_value:
            if neighbor not in states:
                print("State dictionary_neighbour and state_list are not matching")
                print(neighbor, " is not in the states list, ", state_key," , ",state_value)
                return False
    #connection test:
    connection_dict = {}
    for state_key, state_value in neighbors.items():
        for neighbor in state_value:
            connection = ''.join(sorted([state_key, neighbor]))
            #print("Connection: ", connection,connection_dict)
            if connection in connection_dict.keys():
                connection_dict[connection] = connection_dict[connection] + 1
            else:
                connection_dict[connection] = 1
            
    #print(connection_dict)
    for key, value in connection_dict.items():
        if value != 2:
            print("Connection is not valid: ", key)
            return False
               
    return True


def if_the_color_is_suitable(state, color):
    for neighbor in neighbors.get(state):
        #print("State: ", state, " Checking neighbor: ", neighbor, " Neighbour Color: ", colors_of_states.get(neighbor), " Val: ", colors_of_states.get(neighbor) == color)
        if colors_of_states.get(neighbor) == color:
            return False
    return True



def return_the_valid_color(state, start_color_index):
    return_color = None
    index = 0

    if index >= len(colors):
        return_color = None
    else:
        for color in colors[start_color_index:]:
            if if_the_color_is_suitable(state, color):
                return_color = color
                break

            index += 1
            if index >= len(colors):
                return_color = None
                break
        
    if return_color == None:
        print("Go to Backtracking", state, start_color_index)
        last_state, last_state_value = states_where_made_decision_optional.popitem()
        #print("Last State: ", last_state, " Last State Value: ", last_state_value)
        return_color = ['backtrack', last_state, last_state_value]
        #We have to start the loop from here
        #sys.exit(0)
    elif (index != len(colors) - 1):
        states_where_made_decision_optional[state] = return_color
        print("added to the states_where_made_decision_optional: ", state, return_color)

    return return_color




if not check_valid_input():
    print("Please fix the state list and dictionary first")


start_state_index = 0
start_color_index = 0
while start_state_index < len(states):
    state = states[start_state_index]
    output = return_the_valid_color(state,start_color_index)
    print("State: ", state, " Output: ", output)
    #time.sleep(1)
    input("Press Enter to continue...")
    if output[0] == 'backtrack':
        start_state_index = states.index(output[1])
        start_color_index = colors.index(output[2])+1
        print("Start State Index: ", start_state_index, " Start Color Index: ", start_color_index)
        #continue
    else:
        start_color_index = 0
        colors_of_states[state] = output
        start_state_index += 1
    print ("where decision made optionally: ",states_where_made_decision_optional)  


print ("where decision made optionally: ",states_where_made_decision_optional)  
print ("final state of the node: ", colors_of_states)


    
