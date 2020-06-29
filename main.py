import tkinter as tk

class Case:

    CASES = []

    def __init__(self, numberAtoms, i,j):
        self.numberAtoms = numberAtoms
        self.isBorder = False
        self.isCorner = False
        self.i = i
        self.j = j # i et j sont les positions de la case dans la grille 

    def addAtom(self):
        if self.isCorner:
            if self.numberAtoms < 2: self.numberAtoms += 1
            else: self.split()
        elif self.isBorder:
            if self.numberAtoms < 3: self.numberAtoms += 1
            else: self.split()
        else:
            if self.numberAtoms < 4: self.numberAtoms += 1
            else: self.split()

    @classmethod
    def initializeCases(cls, taille):
        cls.CASES = [[Case(0, i, j) for i in range(taille)] for j in range(taille)]
        cls.CASES[0] = [Border(0, 0, j) for j in range(taille)]
        cls.CASES[taille-1] = [Border(0, (taille - 1), j) for j in range(taille)]
        for i in range(taille):
            cls.CASES[i][0] = Border(0, i, 0)
            cls.CASES[i][taille-1] = Border(0, i, (taille - 1))
        cls.CASES[0][0] = Corner(0, 0, 0)
        cls.CASES[0][taille-1] = Corner(0, 0, taille-1)
        cls.CASES[taille-1][0] = Corner(0, taille - 1, 0)
        cls.CASES[taille-1][taille-1] = Corner(0, taille - 1, taille - 1)

    @property
    def adjacentCases(self):
        taille = len(Case.CASES)
        if (self.i, self.j) == (0,0):
            return [Case.CASES[1][0], Case.CASES[0][1]]
        elif (self.i, self.j) == ((taille - 1), 0):
            return [Case.CASES[taille-2][0], Case.CASES[taille-1][1]]
        elif (self.i, self.j) == (0, (taille - 1)):
            return [Case.CASES[0][taille-2], Case.CASES[1][taille-1]]
        elif (self.i, self.j) == ((taille - 1), (taille - 1)):
            return [Case.CASES[taille - 2][taille - 1], Case.CASES[taille - 1][taille - 2]]
        elif self.isBorder:
            if self.i == 0:
                return [Case.CASES[0][self.j + 1], Case.CASES[0][self.j - 1], Case.CASES[1][self.j]]
            elif self.i == taille - 1:
                return [Case.CASES[taille-1][self.j + 1], Case.CASES[taille-1][self.j - 1], Case.CASES[taille-2][self.j]]
            elif self.j == 0:
                return [Case.CASES[self.i + 1][0], Case.CASES[self.i - 1][0], Case.CASES[self.i][1]]
            elif self.j == taille - 1:
                return [Case.CASES[self.i + 1][taille - 1], Case.CASES[self.i - 1][taille - 1], Case.CASES[self.i][taille - 2]]
        else:
            return [Case.CASES[self.i][self.j - 1], Case.CASES[self.i][self.j + 1], Case.CASES[self.i + 1][self.j], Case.CASES[self.i - 1][self.j]]
    
    def split(self):
       self.numberAtoms = 1
       for case in self.adjacentCases:
           case.addAtom()

class Border(Case):

    def __init__(self, numberAtoms, i, j):
        super().__init__(numberAtoms, i, j)
        self.isBorder = True 
        self.isCorner = False

class Corner(Case):

    def __init__(self, numberAtoms, i, j):
        super().__init__(numberAtoms, i, j)
        self.isCorner = True
        self.isBorder = False


def main():
    Case.initializeCases(10)
    print("Tour 1: ")
    print([[(maCase.numberAtoms, maCase.i, maCase.j) for maCase in ligne] for ligne in Case.CASES])
    Case.CASES[0][0].addAtom()
    print("Tour 2: ")
    print([[(maCase.numberAtoms, maCase.i, maCase.j) for maCase in ligne] for ligne in Case.CASES])
    Case.CASES[0][0].addAtom()
    print("Tour 3: ")
    print([[(maCase.numberAtoms, maCase.i, maCase.j) for maCase in ligne] for ligne in Case.CASES])
    Case.CASES[0][0].addAtom()
    print("Tour 4: ")
    print([[(maCase.numberAtoms, maCase.i, maCase.j) for maCase in ligne] for ligne in Case.CASES])

main()