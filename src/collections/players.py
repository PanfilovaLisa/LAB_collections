from src import const

class PlayerCollection:
    def __init__(self):
        self._person = []

    
    def append(self, el):
        const.PLAYER_ID+=1
        return self._person.append(el)
    

    def remove(self, el):
        return self._person.remove(el)


    def pop(self, ind=-1):
        return self._person.pop(ind)
    

    def __len__(self):
        return len(self._person)
    

    def __iter__(self):
        return iter(self._person)
    

    def __getitem__(self, ind):
        return self._person[ind]


    def __str__(self):
        return str(self._person)