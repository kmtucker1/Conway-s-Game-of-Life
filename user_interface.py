
from life import *
from tkinter import *
from tkinter import ttk

#declare global variables
life: Life   
cols = 15
rows = 15

#initial grid that will be used to create the instance of life.py
initial_grid = [[False for i in range(cols)] for j in range(rows)]


def start_game():
    root.destroy()
    game_grid = Tk()

    def SEND():
        for x in range(cols):
            for y in range(rows):
                if life.current_grid[x][y] == True:
                    btn = Button(game_grid, padx=25, pady=25, bg='yellow', command=lambda x=x, y=y: addToArray(x,y))
                    btn.grid(row=x, column=y)
                else:
                    btn = Button(game_grid, padx=25, pady=25)
                    btn.grid(row=x, column=y)
        
        life.create_next_grid()
        game_grid.after(800, SEND)
    SEND()


#create initial grid and life object
root = Tk()
for x in range(cols):
    for y in range(rows):
        def addToArray(x,y):
            initial_grid[x][y] = True
        btn = Button(root, padx=25, pady=25, activebackground='yellow', command=lambda x=x, y=y: addToArray(x,y))
        btn.grid(row=x, column=y)

life = Life(cols, rows, initial_grid)

start_button = Button(root, padx=20, pady=20, text="go", command=start_game)
start_button.grid(row=rows+1, column=cols+1)
root.mainloop()