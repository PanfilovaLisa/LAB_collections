from src import const

class GooseCollection:
    def __init__(self):
        self._geese = [[] for i in range(3)]


    def append(self, el):
        const.GOOSE_ID+=1
        return self._geese.append(el)
    

    def remove(self, el):
        return self._geese.remove(el)


    def pop(self, ind=-1):
        return self._geese.pop(ind)
    

    def SumPower(self):
        return sum(goose.power for goose in self._geese[1])
    

    def __len__(self):
        return len(self._geese)
    

    def __iter__(self):
        return iter(self._geese)
    

    def __getitem__(self, ind):
        return self._geese[ind]


    def __contains__(self, el):
        return el in self._geese


    def __str__(self):
        return str(self._geese)