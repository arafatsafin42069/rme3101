neighbors = {} 
while True:
    input_val = input("Enter state <space> neighbor1 <space> neighbor2 <space> neighbor3 .......... (press exit to cancel): ")
    if input_val == "exit":
        break
    input_val = input_val.split()
    state = input_val[0]
    neighbors[state] = input_val[1:]
    print(neighbors)

print("{")
for key, value in neighbors.items():
    print(f"    {repr(key)}: {repr(value)}")
print("}")
