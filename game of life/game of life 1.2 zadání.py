#https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
#úkoly:

#0. Jak velka je herni plocha?
#0.1 Jak se uklada informace o tom, jestli bunka zije nebo je mrtva?
#1. Dokoncit funkci livingNeighbours()
#2. Napsat 4 podmínky
#5. Udělat posuvník (slider)



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

        
        #speed = w.get()
        speed = 100
        
        self.after(speed, self.update_clock)



def livingNeighbours(x, y):
    living = 0
    if x == 0 or y == 0 or x == rows - 1 or y == cols - 1:
        return 0


    if cells[x-1][y-1] == alive:
        living +=1
    #Ukol 1: Tady bude 7x if


        living = 2
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
            #elif ???
            
                    
            #s vice nez tri sousedy -> umre
            #elif ???
        
            #kazda mrtva s prave tri sousedy -> ozivne
            #elif ???
 
    for i in range(rows):
        for j in range(cols):
            cells[i][j] = cells_new[i][j]



for i in range(rows):
    for j in range(cols):        
        if randint(0,2) == 0:
            cells[i][j] = alive
        else:
            cells[i][j] = dead 


for i in range(rows):
    for j in range(cols):        
        cells_new[i][j] = cells[i][j]



            
window = Tk()

#Ukol 5: Naprogramuje slider pro změnu rychlosti
#5.1: Spusti v jinem projektu tuto ukazku:
#https://python-course.eu/tkinter/sliders-in-tkinter.php
#5.2: Co dela funkce w.set()?
#5.3: Co dela funkce w.get()?
#5.4: V Game of Life zjisti, kde se pouziva w.get()
#5.5: Nastav vhodne tento slider:
#w = Scale(window, from_=???, to=???, orient=???, width= ???, length = ???, label = "???")
#w.set(100)
#w.pack()

app = Window(window)
window.wm_title("Game of Life")
#getting screen width and height of display
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
#setting tkinter window size
window.geometry("%dx%d" % (width, height))


window.mainloop()
