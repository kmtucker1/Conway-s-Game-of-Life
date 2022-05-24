from life import *
from tkinter import *
from tkinter import ttk

    

cols = 10
rows = 10

initial_grid = [[False for i in range(10)] for j in range(rows)]


print(initial_grid)


life = Life(cols, rows, initial_grid)



life.create_next_grid()

print(life.current_grid)



root = Tk()

#create grid
for x in range(10):
    for y in range(10):
        def addToArray(x,y):
            initial_grid[x][y] = True
            print(x)
            print(y)
            print(initial_grid)
        btn = Button(root, padx=20, pady=20, command=lambda x=x, y=y: addToArray(x,y))
        btn.grid(row=x, column=y)
        
            


#def SEND():
 #   print(initial_grid)
#
 #   root.after(500, SEND)
#
#SEND()
root.mainloop()