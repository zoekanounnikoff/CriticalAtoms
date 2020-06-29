import tkinter as tk
import main

class Interface():

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("250x100")
        
        self.bouton_atoms = tk.Button(self.root, text = str(maCase.numberAtoms), bg="white")
        self.bouton_clic = tk.Button(self.root, text="Click here", command = self.clic(), bg="white")

        self.bouton_atoms.pack()
        self.bouton_clic.pack()
        self.root.mainloop()

    def clic(self):
        maCase.addAtom()
        self.bouton_atoms['text'] = str(maCase.numberAtoms)
        
main.Case.initializeCases(8)
maCase = main.Case(0, 1, 5)
interface = Interface()
    


