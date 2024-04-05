import time
import copy

class Grid:
    number_of_columns = 0
    number_of_rows = 0
    def __init__(self, number_of_rows, number_of_columns, terminal_index):
        self.terminal_index = terminal_index
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.grid = [[{'value': 0, 'direction': None} for i in range(number_of_columns)] for j in range(number_of_rows)]
        print("grid created: ", self.grid)
    
    def add_row(self, row_index, row_li):
        for i in range(0, len(row_li)):
            if row_li[i] == None:
                row_li = [None, None]
                pass
            else:
                row_li[i] = {'value': float(row_li[i]), 'direction': None}

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
                column_li[i] = {'value': None, 'direction': None}
                pass
            else:
                column_li[i] = {'value': float(column_li[i]), 'direction': None}

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
        for i in range(self.number_of_rows):
            for j in range(self.number_of_columns):
                if self.grid[i][j]['value'] is not None:
                    # Adjust the width as needed
                    print_statement += "{:7.2f} {}".format(self.grid[i][j]['value'], self.grid[i][j]['direction']) + "\t\t"
                else:
                    print_statement += "{:<7}".format(str(self.grid[i][j]['value'])) + "\t\t"
            print_statement += "\n"
        print_statement += "\n"
        return print_statement

    def get_direction_value(self, row_index, column_index, direction):
        if direction == "up":
            if row_index-1 < 0:
                return float(self.grid[row_index][column_index]['value'])
            
            if self.grid[row_index-1][column_index]['value'] == None:
                return float(self.grid[row_index][column_index]['value'])
            
            return float(self.grid[row_index-1][column_index]['value'])
            
        if direction == "down":
            if row_index+1 >= self.number_of_rows:
                return float(self.grid[row_index][column_index]['value'])
            
            if self.grid[row_index+1][column_index]['value'] == None:
                return float(self.grid[row_index][column_index]['value'])
            
            return float(self.grid[row_index+1][column_index]['value'])


        if direction == "left":
            if column_index-1 < 0:
                return float(self.grid[row_index][column_index]['value'])
            
            if self.grid[row_index][column_index-1]['value'] == None:
                return float(self.grid[row_index][column_index]['value'])
            
            return float(self.grid[row_index][column_index-1]['value'])

        if direction == "right":
            if column_index+1 >= self.number_of_columns:
                return float(self.grid[row_index][column_index]['value'])
            
            if self.grid[row_index][column_index+1]['value'] == None:
                return float(self.grid[row_index][column_index]['value'])
            
            return float(self.grid[row_index][column_index+1]['value'])

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
                if grid.grid[row_no][column_no]['value'] == None:
                    tmp_grid.grid[row_no][column_no] = {'value': None, 'direction': None}

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
                if old_grid_v0.grid[row_no][column_no]['value'] == None:
                    new_grid_v1.grid[row_no][column_no] = {'value': None, 'direction': None}
                    continue
                
                if [row_no,column_no] in old_grid_v0.terminal_index:
                    continue

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
                
                directions = {'up': up, 'down': down, 'left': left, 'right': right}
                max_direction = max(directions, key=directions.get)
                new_grid_v1.grid[row_no][column_no]['value'] = directions[max_direction]
                if directions['up'] == directions['down'] == directions['left'] == directions['right']:
                    #then all the values oare same
                    max_direction = None
                new_grid_v1.grid[row_no][column_no]['direction'] = max_direction

        print("currnet k = ", k, new_grid_v1)
        return new_grid_v1
                    

grid1 = Grid(number_of_rows=3, number_of_columns=4, terminal_index=[[0,3],[1,3]])
grid1.add_column(0, [0, 0, 0])
grid1.add_column(1, [0, None, 0])
grid1.add_column(2, [0, 0, 0])
grid1.add_column(3, [+1, -1, 0])
print(grid1.grid)

calculate_mdp(grid = grid1,  noise=0.2, discount=0.9, living_reward=0, k=100)
