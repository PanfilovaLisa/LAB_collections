class CEILS:
    def __init__(self):
        self._CEILS = []


    def append(self, ceil):
        return self._CEILS.append(ceil)
    

    def __iter__(self):
        return iter(self._CEILS)


    def __len__(self):
        return len(self._CEILS)


    def __getitem__(self, ind):
        return self._CEILS[ind]


    def __str__(self):
        return str(self._CEILS)
    

class Ceil:
    def __init__(self, name: str):
        self.name = name 
        self.bets = []

    
    def AddBet(self, player: str, bet: list):
        return self.bets.append((player, bet))
    

    def GetBets(self):
        return self.bets


    def __iter__(self):
        return iter(self.bets)
    

    def clear(self):
        return self.bets.clear()

    
    def __str__(self):
        return str(self.bets)
    