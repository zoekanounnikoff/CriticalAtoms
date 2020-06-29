import tkinter as tk

class Case:

    CASES = []

    def __init__(self, numberAtoms):
        self.numberAtoms = numberAtoms
        self.isBorder = False
        self.isCorner = False

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
        cls.CASES = [[Case(0) for i in range(taille)] for j in range(taille)]
        cls.CASES[0][0] = Corner(0)
        cls.CASES[0][taille-1] = Corner(0)
        cls.CASES[taille-1][0] = Corner(0)
        cls.CASES[taille-1][taille-1] = Corner(0)

    
    def split(self):
        pass

class Border(Case):

    def __init__(self, numberAtoms):
        super().__init__(numberAtoms)
        self.isBorder = True
        self.isCorner = False
class Corner(Case):

    def __init__(self, numberAtoms):
        super().__init__(numberAtoms)
        self.isCorner = True
        self.isBorder = False


def main():
    Case.initializeCases(10)
    print(Case.CASES)

main()