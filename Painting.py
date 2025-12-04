import tkinter as tk
from tkinter import colorchooser

def vyber_barvu():
    barva = colorchooser.askcolor(title="Vyber barvu")
    barva_button.config(fg=barva[1])

#okno
root = tk.Tk()
root.title("Malování")
root.minsize(750, 500)
root.maxsize(750, 500)

#vlozeni platna
platno = tk.Canvas(root,width=750,height=450,bg="lightgrey")
platno.grid(row=1, columnspan=10, padx=3, pady=3)

#barva
barva_button = tk.Button(root, text="Barva", command=vyber_barvu, width=10)
barva_button.grid(row=0, column=0, padx=3, pady=3)

#velikost
velikost_spinbox = tk.Spinbox(root, from_=4, to=40, width=5)
velikost_spinbox.grid(row=0, column=1, padx=3, pady=3)

#moznosti
styl_podtrzeni = ["tužka","sprej","obdelník","kruh", "guma"]
vybrany_styl_podtrzeni = tk.StringVar(value=styl_podtrzeni[0])
styl_optionmenu = tk.OptionMenu(root, vybrany_styl_podtrzeni, *styl_podtrzeni)
styl_optionmenu.grid(row=0, column=2, padx=3, pady=3)

#zmazání plátna
def smaz_platno():
    platno.delete("all")

button_smaz = tk.Button(root,text="smazat", command=smaz_platno)
button_smaz.grid(row=0, column=3, padx=3, pady=3)

root.mainloop()