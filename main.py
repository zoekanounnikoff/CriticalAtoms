class Case:

    def __init__(self, numberAtoms):
        self.numberAtoms = numberAtoms

    def addAtom(self):
        if self.numberAtoms < 3:
            self.numberAtoms += 1

class Border(Case):
    def __init__(self, numberAtoms):
        super().__init__()

class Corner(Border):
    def __init__():
        

maCase = Case(3)
print(maCase.numberAtoms)