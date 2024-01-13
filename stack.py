stack = []
limit = 1000
starting_index = 0
top = starting_index - 1


def push(a):
    global top, stack, limit
    top = top + 1
    if len(stack) > limit:
        print("Not available space:")
        return -1
    else:
        stack.insert(top, a)
        print("Data inserted successfully: ", stack, " at index(top): ", top)

def pop():
    global top, stack
    if top == -1:
        print("Not available data")
        return -1
    
    stack = stack[:top]
    print("Data popped succesfully: ", stack, " at index(top): ", top)
    top = top - 1

def clear_stack():
    global top, stack
    top = -1
    stack.clear()

def check_pldrm():
    for i in range(0,int(len(stack)/2)):
        if(stack[starting_index + i] != stack[starting_index + len(stack)-1-i]):
            return -1
            break
        
    return 1


# while True:
#     c = input("Enter the command 1 for push 2 for pop: ")
#     if(c == "1"):
#         data = input("Enter the Data: ")
#         for c in data:
#             push(c)
#     if( c == "2"):
#         pop()
    





# file1 = open('lab1.txt', 'r')
# Lines = file1.readlines()
# print(Lines)

# for line in Lines:
#     print(line)
#     if line[0] == "1" :
#         line = line[1:].strip()
#         for c in line:
#             push(c)

#     if line[0] == "2" :
#         pop()


file1 = open('input.txt', 'r')
Lines = file1.readlines()
print(Lines)

numbers_of_input = Lines[0].strip()

for line in Lines[1:]:
    line = line.strip()
    line = line.lower()
    print(line)
    for c in line:
        push(c)

    if check_pldrm() == -1:
        print("Not Pallindrome")
    if check_pldrm() == 1:
        print("Pallindrome")
    

    clear_stack()

    
