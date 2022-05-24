from life import *
from tkinter import *
from tkinter import ttk

cols = 10
rows = 10

grid = [[False for i in range(cols)] for j in range(rows)]


grid[0][0] = True
grid[1][1] = True
grid[2][2] = True
grid[3][3] = True
grid[3][4] = True
grid[4][4] = True


print(grid)


life = Life(cols, rows, grid)



life.create_next_grid()

print(life.current_grid)



root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


#example values
for x in range(10):
    for y in range(10):
        btn = Button(root)
        btn.grid(column=x, row=y, sticky="news")

root.columnconfigure(tuple(range(cols)), weight=1)
root.rowconfigure(tuple(range(rows)), weight=1)

def SEND():
    

    root.after(500, SEND)

SEND()
root.mainloop()