import tkinter
import random

window = tkinter.Tk()

window.geometry("700x300")

button = tkinter.Button(window, text = "Klikni na mě!", width=40)
button.pack(padx=10, pady=10)

pocetKliku = 0
pocetPokusu = 0

def onClick(event):
    global pocetKliku
    pocetKliku = pocetKliku + 1
    if pocetKliku >1:
        button.configure(text="Jseš fakt dobrej")
        
def onEnter(event):
    button.place(x=random.randint(0, 600), y=random.randint(0, 200))
    button.configure(text="Vedle")

button.bind("<ButtonRelease-1>", onClick)
button.bind('<Enter>', onEnter)

window.mainloop()

    
