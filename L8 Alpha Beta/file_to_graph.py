def find_terminal_node_value(path):
    # {"P": 3, "Q": 4, "R" : 2}
    #this is the example
    terminal_state_value = {}
    with open(path, 'r') as file:
        lines = file.readlines()
        #print(lines)

    line_1 = []
    for line in lines:
        line = line.strip()
        line_1.append(line)
    
    #print(line_1)

    number_of_line = int(line_1[0])
    #print("number of ines: ",number_of_line)

    for line in line_1[1:]:
        key, value = line.split()
        terminal_state_value[key] = int(value)
    #print(terminal_state_value)
    return terminal_state_value

def find_input_graph(graph_path, terminal_path):
    input_graph = {}
    with open(graph_path, 'r') as file:
        lines = file.readlines()
        #print(lines)

    number_of_line = int(lines[0].strip())
    
    for line in lines[1:]:
        line = line.strip()
        #print(line)
        line_li = line.split(" ")
        key = line_li[0]
        value = line_li[1:]
        #print(key, value)
        input_graph[key] = value

    with open(terminal_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        line_li = line.split(" ")
        key = line_li[0]
        input_graph[key] = ""


    return input_graph

    


print(find_terminal_node_value("C:\\Users\\Acer\\OneDrive\\Desktop\\3111\\L8 Alpha Beta\\input_terminal.txt"))
print(find_input_graph("C:\\Users\\Acer\\OneDrive\\Desktop\\3111\\L8 Alpha Beta\\input_map.txt","C:\\Users\\Acer\\OneDrive\\Desktop\\3111\\L8 Alpha Beta\\input_terminal.txt"))