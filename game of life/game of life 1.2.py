#https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

from array import *
from random import *
from tkinter import *



rows = 52
cols = 123
speed = 80
alive = "■"
dead  = '\0'

generation = 0
cells  = [ [0]*cols for i in range(rows)]
cells_new  = [ [0]*cols for i in range(rows)]


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.label_dict = {}       
        for i in range(rows):
            self.label_dict[i] = Label(text="", fg="Green", font=("Consolas", 7))
            m = 11*i + 50
            self.label_dict[i].place(x=15, y=m)

        self.label_title = Label(text="Game of Life", fg="Red", font=("Consolas", 14))
        self.label_title.place(x=15, y=5)

        self.label_title = Label(text="", fg="Blue", font=("Consolas", 10))
        self.label_title.place(x=15, y=25)
        
        self.update_clock()

    def update_clock(self):
        global generation
        
        for i in range(rows):
            now = cells[i]
            self.label_dict[i].configure(text=now)

        now2 = "Generation: " + str(generation)
        self.label_title.configure(text=now2)
        nextGeneration()
        generation += 1

        speed = w.get()
        self.after(speed, self.update_clock)



def livingNeighbours(x, y):
    living = 0
    #global alive
    if x == 0 or y == 0 or x == rows - 1 or y == cols - 1:
        return 0
    
    if cells[x-1][y-1] == alive:
        living +=1
    if cells[x][y-1]   == alive:
        living +=1
    if cells[x+1][y-1] == alive:
        living +=1
    if cells[x-1][y]   == alive:
        living +=1
    if cells[x+1][y]   == alive:
        living +=1
    if cells[x-1][y+1] == alive:
        living +=1
    if cells[x][y+1]   == alive:
        living +=1
    if cells[x+1][y+1] == alive:
        living +=1

    return living
    

def printCells(cells):   
    for i in range(len(cells)):
        print(cells[i])
        
      
def nextGeneration():
    global cells          
    for x in range(rows):
        for y in range(cols):
            neighbours = livingNeighbours(x, y)                
            #mene nez dva zive sousedy -> umre
            if cells[x][y] == alive and neighbours < 2:
                cells_new[x][y] = dead
        
            #dva nebo tri sousedy -> prezije
            elif cells[x][y] == alive and  (neighbours == 2 or neighbours == 3):
                cells_new[x][y] = alive
                    
            #s vice nez tri sousedy -> umre
            elif cells[x][y] == alive and neighbours > 3:
                cells_new[x][y] = dead
        
            #kazda mrtva s prave tri sousedy -> ozivne
            elif cells[x][y] == dead and neighbours == 3:
                cells_new[x][y] = alive
 
    for i in range(rows):
        for j in range(cols):
            cells[i][j] = cells_new[i][j]




for i in range(rows):
    for j in range(cols):        
        if randint(0,2) == 0:
            cells[i][j] = alive
        else:
            cells[i][j] = dead 

'''
#Middle-weight spaceship(MWSS)
cells[10][10] = alive
cells[10][11] = alive
cells[10][12] = alive
cells[10][13] = alive
cells[10][14] = alive
cells[11][9] = alive
cells[11][14] = alive
cells[12][14] = alive
cells[13][9] = alive
cells[13][13] = alive
cells[14][11] = alive
'''
'''
#Gosper glider gun
cells[12][36] = alive
cells[13][34] = alive
cells[13][36] = alive

cells[14][24] = alive
cells[14][25] = alive
cells[14][32] = alive
cells[14][33] = alive

cells[15][46] = alive
cells[15][46] = alive
cells[16][46] = alive
cells[16][47] = alive

cells[15][23] = alive
cells[15][27] = alive
cells[15][32] = alive
cells[15][33] = alive

cells[17][12] = alive
cells[17][13] = alive
cells[16][22] = alive
cells[16][28] = alive
cells[16][32] = alive
cells[16][33] = alive

cells[18][12] = alive
cells[18][13] = alive
cells[17][22] = alive
cells[17][26] = alive
cells[17][28] = alive
cells[17][29] = alive
cells[17][34] = alive
cells[17][36] = alive

cells[18][22] = alive
cells[18][28] = alive
cells[18][36] = alive

cells[19][23] = alive
cells[19][27] = alive

cells[20][24] = alive
cells[20][25] = alive
'''









for i in range(rows):
    for j in range(cols):        
        cells_new[i][j] = cells[i][j]
            
window = Tk()
w = Scale(window, from_=1, to=1000, orient=HORIZONTAL, width= 10, length = 200, label = "Delay (ms)")
w.set(100)
w.pack()

app = Window(window)
window.wm_title("Game of Life")
#getting screen width and height of display
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
#setting tkinter window size
window.geometry("%dx%d" % (width, height))


window.mainloop()
