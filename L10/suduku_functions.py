import time
import math 

def print_sudoku(puzzle): 
    for i in range(9): 
        if i % 3 == 0 and i != 0: 
            print("- - - - - - - - - - - ") 
        for j in range(9): 
            if j % 3 == 0 and j != 0: 
                print(" | ", end="") 
            print(puzzle[i][j], end=" ") 
        print() 
  
def find_variables():
    list_of_variables = []
    for i in range(0,9):
        for j in range(0,9):
            list_of_variables.append((i,j))

    #print(list_of_variables)
    return list_of_variables

def divide_by_row_and_column(puzzle):
    dict_row_column = {"row": [], "column": []}
    for i in range(0,9):
        dict_row_column["row"].append(puzzle[i])
    #print("Rows: ", dict_row_column['row'])

    for i in range(0,9):
        dict_row_column["column"].append([])

    for i in range(0,9):
        #this will control the row no
        for j in range(0,9):
            #this will control the column nodf
            dict_row_column["column"][j].append(puzzle[i][j])

    #print("Column: ", dict_row_column["column"])
    return dict_row_column




def find_domains(puzzle):
    row_column_dict = divide_by_row_and_column(puzzle=puzzle)
    dict_of_domain = {}

    for i in range(0,9):
        for j in range(0,9):
            #i means row
            #j means column in that row
            dict_of_domain[(i,j)] = []

    for i in range(0,9):
        for j in range(0,9):
            if puzzle[i][j] != 0:
                dict_of_domain[(i,j)] = [puzzle[i][j]]
                continue

            dict_of_domain[(i,j)] = list(range(1,10))
    
    #for key,value in dict_of_domain.items():
        #print(key," : ",value)
    return dict_of_domain
        
def find_constrains():
    constrains_dict = {}
    for i in range(0,9):
        for j in range(0,9):
            constrains_dict[(i,j)] = []

    for i in range(0,9):
        for j in range(0,9):
            for x in range(0,9):
                constrains_dict[(i,j)].append((i,x))
            for x in range(0,9):
                constrains_dict[(i,j)].append((x,j))
    
    for i in range(9):
        for j in range(9):
            subgrid_row = 3 * (i // 3) #this will be the floow value
            subgrid_col = 3 * (j // 3) #this will be the floor value
            for x in range(subgrid_row, subgrid_row + 3):
                for y in range(subgrid_col, subgrid_col + 3):
                    constrains_dict[(i,j)].append((x,y))

    for key, value in constrains_dict.items():
        value = set(value)

    for i in range(9):
        for j in range(9):
                constrains_dict[(i,j)].remove((i,j))
                    
    with open("constrains_dict.txt", "w") as file:
        for key, value in constrains_dict.items():
            file.write(f"{key}: {value}\n")
            
            

    return constrains_dict
