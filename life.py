from xmlrpc.client import boolean



#global variables for size of window
cols: int = 10
rows: int = 10


#current grid array
current_grid: boolean = [[0]*cols]*rows


#next grid array
next_grid: boolean = [[0]*cols]*rows



#interates through array grid and determines what the next grid will look like according to rules of game of life
for i in range(len(current_grid)):
    for j in range(len(current_grid[i])):
        #number of neighbors cell has
        neighbor_count: int = 0
        #current status of cell
        status: boolean = current_grid[i][j]



        #count number of neighbors for current cell

        #left cell
        if (j - 1) >= 0:
            if current_grid[i][j-1] == True:
                neighbor_count += 1
        #top-left cell
        if (j - 1) >= 0 and (i - 1) >= 0:
            if current_grid[i-1][j-1] == True:
                neighbor_count += 1
        #top cell
        if (i - 1) >= 0:
            if current_grid[i-1][j] == True:
                neighbor_count += 1
        #top-right cell
        if (i - 1) >= 0 and (j + 1) < cols:
            if current_grid[i-1][j+1] == True:
                neighbor_count += 1
        #right cell
        if (j + 1) < cols:
            if current_grid[i][j+1] == True:
                neighbor_count += 1
        #bottom-right cell
        if (j + 1) < cols and (i + 1) < rows:
            if current_grid[i+1][j+1] == True:
                neighbor_count += 1
        #bottom cell
        if (i + 1) < rows:
            if current_grid[i+1][j] == True:
                neighbor_count += 1
        #bottom-left cell
        if (i + 1) < rows and (j - 1) > 0:
            if current_grid[i+1][j-1]:
                neighbor_count += 1



        #if cell is alive has 2 neighbors, it lives
        if neighbor_count == 2 and status == True:
            next_grid[i][j] == True
        #if cell has 3 neighbors, it lives regardless whether it was alive before or now
        if neighbor_count == 3:
            next_grid[i][j] == True
        #else cell dies



#create new grid
