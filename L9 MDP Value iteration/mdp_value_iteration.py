import time
import copy

class Grid:
    number_of_columns = 0
    number_of_rows = 0
    def __init__(self, number_of_rows, number_of_columns, terminal_index):
        self.terminal_index = terminal_index
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.grid = [[0 for i in range(number_of_columns)] for j in range(number_of_rows)]
        print("grid created: ", self.grid)
    
    def add_row(self, row_index, row_li):
        for i in range(0, len(row_li)):
            if row_li[i] == None:
                pass
            else:
                row_li[i] = float(row_li[i])

        if row_index < 0 or row_index >= self.number_of_rows:
            raise ValueError("Row index is out of range.")
        
        if len(row_li) != self.number_of_columns:
            raise ValueError("This row doesn't have the same length as the number of columns.")
        
        self.grid[row_index] = row_li
        print("Row added: ")
        print(self)

    def add_column(self, column_index, column_li):
        for i in range(0, len(column_li)):
            if column_li[i] == None:
                pass
            else:
                column_li[i] = float(column_li[i])

        if column_index < 0 or column_index >= self.number_of_columns:
            raise ValueError("Column index is out of range")

        if len(column_li) != self.number_of_rows:
            raise ValueError("This column doesn't have the same length as the number of rows.")

        for i in range(0, self.number_of_rows):
            self.grid[i][column_index] = column_li[i]

        print("Column added: ")
        print(self)

    def __str__(self):
        print_statement = "\n"
        for i in range(0, self.number_of_rows):
            for j in range(0, self.number_of_columns):
                if self.grid[i][j] != None:
                    print_statement = print_statement + "{:0.2f}".format(self.grid[i][j])+ "\t" #+ str(type(self.grid[i][j])) + "\t"
                else:
                    print_statement = print_statement + str(self.grid[i][j])+ "\t" #+ str(type(self.grid[i][j])) + "\t"
            print_statement = print_statement + "\n"
        print_statement = print_statement + "\n"
        return print_statement

    def get_direction_value(self, row_index, column_index, direction):
        if direction == "up":
            if row_index-1 < 0:
                return float(self.grid[row_index][column_index] )
            
            if self.grid[row_index-1][column_index] == None:
                return float(self.grid[row_index][column_index] )
            
            return float(self.grid[row_index-1][column_index] )
            
        if direction == "down":
            if row_index+1 >= self.number_of_rows:
                return float(self.grid[row_index][column_index] )
            
            if self.grid[row_index+1][column_index] == None:
                return float(self.grid[row_index][column_index])
            
            return float(self.grid[row_index+1][column_index] )


        if direction == "left":
            if column_index-1 < 0:
                return float(self.grid[row_index][column_index] )
            
            if self.grid[row_index][column_index-1] == None:
                return float(self.grid[row_index][column_index])
            
            return float(self.grid[row_index][column_index-1] )

        if direction == "right":
            if column_index+1 >= self.number_of_columns:
                return float(self.grid[row_index][column_index] )
            
            if self.grid[row_index][column_index+1] == None:
                return float(self.grid[row_index][column_index])
            
            return float(self.grid[row_index][column_index+1] )

def print_quat(value, up, down, left, right):
    print("value: ", value)
    print("\t",up,"\t")
    print(left,"\t\t",right)
    print("\t",down,"\t")
    print()
    inp = input()

def calculate_mdp(grid, noise, discount, living_reward, k):   
    if k == 0:
        tmp_grid = Grid(grid.number_of_rows, grid.number_of_columns, [])
        for row_no in range(0, grid.number_of_rows):
            for column_no in range(0, grid.number_of_columns):
                if grid.grid[row_no][column_no] == None :
                    tmp_grid.grid[row_no][column_no] = None

        print("currnet k = ", k, tmp_grid)
        return grid
    elif k == 1:
        calculate_mdp(grid, noise, discount, living_reward, k-1)
        print("currnet k = ", k, grid)
        return grid
    else:
        old_grid_v0 = calculate_mdp(copy.deepcopy(grid), noise, discount, living_reward, k-1)
        new_grid_v1 = copy.deepcopy(grid)

        for row_no in range(0, old_grid_v0.number_of_rows):
            for column_no in range(0, old_grid_v0.number_of_columns):
                if old_grid_v0.grid[row_no][column_no] == None :
                    new_grid_v1.grid[row_no][column_no] = None
                    continue
                
                if [row_no,column_no] in old_grid_v0.terminal_index:
                    continue

                # print("row: ", row_no, "column: ", column_no)
                # print("up ",old_grid_v0.get_direction_value(row_no, column_no, "up"))
                # print("donwn ",old_grid_v0.get_direction_value(row_no, column_no, "down"))
                # print("left ", old_grid_v0.get_direction_value(row_no, column_no, "left"))
                # print("right ", old_grid_v0.get_direction_value(row_no, column_no, "right"))
                
                up = ((1 - noise)*(living_reward + discount * old_grid_v0.get_direction_value(row_no, column_no, "up"))
                      +(noise/2)*(living_reward + discount * old_grid_v0.get_direction_value(row_no, column_no, "left"))
                      +(noise/2)*(living_reward + discount * old_grid_v0.get_direction_value(row_no, column_no, "right")))
                #print(up)

                down = ((1 - noise)*(living_reward + discount * old_grid_v0.get_direction_value(row_no, column_no, "down"))
                      +(noise/2)*(living_reward + discount * old_grid_v0.get_direction_value(row_no, column_no, "left"))
                      +(noise/2)*(living_reward + discount * old_grid_v0.get_direction_value(row_no, column_no, "right")))
                #print(down)

                left = ((1 - noise)*(living_reward + discount * old_grid_v0.get_direction_value(row_no, column_no, "left"))
                      +(noise/2)*(living_reward + discount * old_grid_v0.get_direction_value(row_no, column_no, "up"))
                      +(noise/2)*(living_reward + discount * old_grid_v0.get_direction_value(row_no, column_no, "down")))
                #print(left)

                right = ((1 - noise)*(living_reward + discount * old_grid_v0.get_direction_value(row_no, column_no, "right"))
                      +(noise/2)*(living_reward + discount * old_grid_v0.get_direction_value(row_no, column_no, "up"))
                      +(noise/2)*(living_reward + discount * old_grid_v0.get_direction_value(row_no, column_no, "down")))
                #print(right)
                

               
                #inp = input()
                new_grid_v1.grid[row_no][column_no] = max(up, down, left, right)


        print("currnet k = ", k, new_grid_v1)
        return new_grid_v1
                    

grid1 = Grid(number_of_rows=3, number_of_columns=4, terminal_index=[[0,3],[1,3]])
grid1.add_column(0, [0, 0, 0])
grid1.add_column(1, [0, None, 0])
grid1.add_column(2, [0, 0, 0])
grid1.add_column(3, [+1, -1, 0])
print(grid1.grid)

calculate_mdp(grid = grid1,  noise=0.2, discount=0.9, living_reward=0, k=100)