from src.chips import chiplist
from src.animals import human, gooses
import random

class Simulation:
    def __init__(self, casino):
        self.Casino = casino 
        self.Actions = [self.CreateGoose, self.CreatePlayer, self.CallHonkGoose, self.PlayersBuyChips, self.PlayRound, self.GooseInspection]


    def CreatePlayer(self):
        balance = random.randint(10, 1000)
        chips = chiplist.ChipList()
        player = human.Player(balance = balance, chips=chips, scared=False)
        self.Casino.AddPlayer(player)
        return True
    

    def CreateGoose(self, type = random.randint(0, 2)):
        balance = random.randint(0, 1000)
        if type==0:
            goose = gooses.Goose(balance=balance)
        elif type==1:
            power=random.randint(1, 5)
            goose = gooses.WarGoose(balance=balance, power=power)
        else:
            Honk_volume=random.randint(1, 5)
            goose = gooses.HonkGoose(Honk_volume=Honk_volume, balance=balance)
        self.Casino.AddGoose(goose)
        return True


    def CallHonkGoose(self):
        player_index = random.randint(0, len(self.Casino.PlayersCollection)-1)
        player = self.Casino.PlayersCollection[player_index]

        goose_index = random.randint(0, len(self.Casino.GeeseCollection[2])-1)
        goose = self.Casino.GeeseCollection[2][goose_index]

        self.Casino.CallHonkGoose(goose=goose, player=player)
        return True


    def PlayersBuyChips(self):
        player_index = random.randint(0, len(self.Casino.PlayersCollection)-1)
        player = self.Casino.PlayersCollection[player_index]

        self.Casino.PlayerBuyChip(player=player)
        return True


    def PlayRound(self):
        self.Casino.PlayRound()
        return True

    
    def GooseInspection(self):
        self.Casino.CheckPlayers()
        return True
    

    def run_simulation(self, seed, steps: int=20) -> None:
        ActionsVarioants=len(self.Actions)
        random.seed(seed)
        for step in range(steps):
            action = random.randint(0, ActionsVarioants-1)
            self.Actions[action]()
        return True
        

