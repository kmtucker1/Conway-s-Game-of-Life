
from xmlrpc.client import boolean


class Life:

    #global variables for size of window
    cols: int = 10
    rows: int = 10

    #current grid
    current_grid: boolean


    def __init__(self, cols: int, rows: int, current_grid):
        self.current_grid = current_grid
        self.cols = cols
        self.rows = rows



    #interates through array grid and determines what the next grid will look like according to rules of game of life
    def create_next_grid(self):
        #next grid array
        next_grid: boolean = [[False for i in range(self.cols)] for j in range(self.rows)]

        for i in range(len(self.current_grid)):
            for j in range(len(self.current_grid[i])):
                #number of neighbors cell has
                neighbor_count: int = 0
                #current status of cell
                status: boolean = self.current_grid[i][j]



                #count number of neighbors for current cell

                #left cell
                if (j - 1) >= 0:
                    if self.current_grid[i][j-1] == True:
                        neighbor_count += 1
                #top-left cell
                if (j - 1) >= 0 and (i - 1) >= 0:
                    if self.current_grid[i-1][j-1] == True:
                        neighbor_count += 1
                #top cell
                if (i - 1) >= 0:
                    if self.current_grid[i-1][j] == True:
                        neighbor_count += 1
                #top-right cell
                if (i - 1) >= 0 and (j + 1) < self.cols:
                    if self.current_grid[i-1][j+1] == True:
                        neighbor_count += 1
                #right cell
                if (j + 1) < self.cols:
                    if self.current_grid[i][j+1] == True:
                        neighbor_count += 1
                #bottom-right cell
                if (j + 1) < self.cols and (i + 1) < self.rows:
                    if self.current_grid[i+1][j+1] == True:
                        neighbor_count += 1
                #bottom cell
                if (i + 1) < self.rows:
                    if self.current_grid[i+1][j] == True:
                        neighbor_count += 1
                #bottom-left cell
                if (i + 1) < self.rows and (j - 1) > 0:
                    if self.current_grid[i+1][j-1]:
                        neighbor_count += 1




                #determine status of current cell in next grid
                
                #if cell is alive has 2 neighbors, it lives
                if neighbor_count == 2 and status == True:
                    
                    next_grid[i][j] = True
                    #if cell has 3 neighbors, it lives regardless whether it was alive before or now
                elif neighbor_count == 3:
                    next_grid[i][j] = True
                #else cell dies
                else:
                    next_grid[i][j] = False
        #update grid
        self.current_grid = next_grid
        

