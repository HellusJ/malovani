import tkinter as tk
from tkinter import colorchooser
import random as rd

hex = "#000000"
def vyber_barvu():
    global hex
    barva = colorchooser.askcolor(title="Vyber barvu")
    barva_button.config(fg=barva[1])
    hex = barva[1]

# okno
root = tk.Tk()
root.title("Malování")
root.minsize(750, 500)
root.maxsize(750, 500)

# vlozeni platna
platno = tk.Canvas(root, width=750, height=500, bg="lightgrey")
platno.grid(row=1, columnspan=8)

# barva
barva_button = tk.Button(root, text="Barva", command=vyber_barvu, width=10)
barva_button.grid(row=0, column=0, padx=3, pady=3)

# velikost
velikost_spinbox = tk.Spinbox(root, from_=4, to=200, width=5)
velikost_spinbox.grid(row=0, column=1, padx=3, pady=3)

# moznosti
styl_podtrzeni = ["tužka","sprej","obdelník","kruh", "guma"]
vybrany_styl_podtrzeni = tk.StringVar(value=styl_podtrzeni[0])
styl_optionmenu = tk.OptionMenu(root, vybrany_styl_podtrzeni, *styl_podtrzeni)
styl_optionmenu.grid(row=0, column=2, padx=3, pady=3)

# tuzka
posledni_x = None
posledni_y = None

def zacni_kreslit(mys):
    global posledni_x, posledni_y
    posledni_x = mys.x
    posledni_y = mys.y

def kresli(mys):
    global posledni_x, posledni_y

    if posledni_x is None or posledni_y is None:
        posledni_x = mys.x
        posledni_y = mys.y
        return 0

    platno.create_line(posledni_x, posledni_y, mys.x, mys.y,fill=hex, smooth=True, capstyle="round",width=int(velikost_spinbox.get()))
    posledni_x = mys.x
    posledni_y = mys.y

def sprej(mys):
    hustota = 10
    r=1
    for i in range(hustota):
        dx = rd.randint(-20, 20)
        dy = rd.randint(-20, 20)

        x = mys.x + dx
        y = mys.y + dy

        platno.create_oval(x - r, y - r, x + r, y + r, fill=hex, outline="")

def guma(mys):
    global posledni_x, posledni_y

    if posledni_x is None or posledni_y is None:
        posledni_x = mys.x
        posledni_y = mys.y
        return 0

    platno.create_line(posledni_x, posledni_y, mys.x, mys.y,fill="lightgrey", smooth=True, capstyle="round",width=int(velikost_spinbox.get()))
    posledni_x = mys.x
    posledni_y = mys.y

def stop_kresleni(*args):
    global posledni_x, posledni_y
    posledni_x = None
    posledni_y = None

def aktualizuj_bind(*args): 
    platno.unbind("<Button-1>")
    platno.unbind("<B1-Motion>")
    platno.unbind("<ButtonRelease-1>")

    styl = vybrany_styl_podtrzeni.get()

    if styl == "tužka":
        platno.bind("<Button-1>", zacni_kreslit)
        platno.bind("<B1-Motion>", kresli)
        platno.bind("<ButtonRelease-1>", stop_kresleni)

    elif styl == "sprej":
        platno.bind("<Button-1>", sprej)
        platno.bind("<B1-Motion>", sprej)
    
    elif styl == "guma":
        platno.bind("<Button-1>", zacni_kreslit)
        platno.bind("<B1-Motion>", guma)
        platno.bind("<ButtonRelease-1>", stop_kresleni)

vybrany_styl_podtrzeni.trace("w", aktualizuj_bind)
aktualizuj_bind()  

def smaz_platno():
    platno.delete("all")

button_smaz = tk.Button(root, text="smazat", command=smaz_platno)
button_smaz.grid(row=0, column=3, padx=3, pady=3)

root.mainloop()

