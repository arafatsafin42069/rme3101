def file_to_graph(path):
    all_node =[]
    input_graph = {}
    terminal_state_value = {}
    with open(path, 'r') as file:
        lines = file.readlines()
        #print(lines)
    first_line = lines[0].split()
    number_of_connections = int(first_line[0])
    initial_node = first_line[1].strip()
    print(number_of_connections, initial_node)
    for i in range(1,number_of_connections+1):
        line = lines[i].strip()
        line_li = line.split(" ")
        key = line_li[0]
        value = line_li[1:]
        input_graph[key] = value
        all_node.append(key)

    print(input_graph)

    for i in range(number_of_connections+2, len(lines)):
        line = lines[i].split(" ")
        #print(line)
        key = line[0]
        value = int(line[1].strip())
        terminal_state_value[key] = int(value)
        all_node.append(key)
        input_graph[key] = ""

    print(terminal_state_value)
    print(all_node)

    return input_graph, terminal_state_value, all_node

file_to_graph("C:\\Users\\Acer\\OneDrive\\Desktop\\3111\\L8 Alpha Beta\\input_text1.txt")
    