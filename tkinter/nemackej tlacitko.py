import tkinter
window = tkinter.Tk()

button = tkinter.Button(window, text = "Nemačkej tohle tlačítko!", width=40)
button.pack(padx=10, pady=10)

pocetKliku = 0

def onClick(event):
        global pocetKliku
        pocetKliku = pocetKliku + 1
        if pocetKliku ==1:
            button.configure(text="Jako vážně? Ne-mač-kej to!")
        elif pocetKliku ==2:
            button.configure(text="Fakt mě štveš!")
        elif pocetKliku ==3:
            button.configure(text="Grrr. Příště nebude žádné tlačítko!")
        else:
                button.pack_forget()

button.bind("<ButtonRelease-1>", onClick)
window.mainloop()


    
