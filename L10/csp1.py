neighbors = {
    'WA' : ['NT', 'SA'],
    'NT' : ['WA', 'SA', 'Q'],
    'SA' : ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q' :  ['NT', 'SA', 'NSW'],
    'NSW' :  ['Q', 'SA','V'],
    'V' :  ['NSW', 'SA'],
    'T' :  ['']
}

colors = ['Red', 'Blue', 'Green']

states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

states_where_made_decision_optional = []

colors_of_states = {}


def check_valid_input():
    for neighbor in neighbors:
        if neighbor not in states:
            print ("Invalid input")
            print("Problem with: ", neighbor, "Not in states")
            return False
        neighbor_list = neighbors.get(neighbor)
        for n in neighbor_list:
            if n not in states:
                if n == '':
                    continue
                print ("Invalid input")
                print("Problem with: ", n, "Not in states")
                return False
    return True

def if_the_color_is_suitable(state, color):
    for neighbor in neighbors.get(state):
        #print("State: ", state, " Checking neighbor: ", neighbor, " Neighbour Color: ", colors_of_states.get(neighbor), " Val: ", colors_of_states.get(neighbor) == color)
        if colors_of_states.get(neighbor) == color:
            return False
    return True



def return_the_valid_color(state):
    return_color = None
    index = 0
    for color in colors:
        # print("Checking color: ", color)
        # print(colors_of_states)
        #print(if_the_color_is_suitable(state, color))
        if if_the_color_is_suitable(state, color):
            return_color = color
            break

        index += 1
    if index != len(colors) - 1:
        states_where_made_decision_optional.append(state)
    return return_color




if not check_valid_input():
    print("Please fix the neighbors list")
for state in states:
    colors_of_states[state] = return_the_valid_color(state)

print (colors_of_states)
print (states_where_made_decision_optional)  
    
