from src import const, log
from src.chips import chip

class Player:

    def __init__(self, balance: int, scared: bool, chips: list, id = const.PLAYER_ID, ):
        self.player_id = "P" + str(const.PLAYER_ID)
        self.balance = balance
        self.ChipList = chips


    def BuyChip(self, CHIPS):
        chip_color = sorted([color for color in CHIPS if (self.balance - CHIPS[color]) >= 0])[0]
        Chip = chip.Chip(color=chip_color, CHIPS=CHIPS)
        self.ChipList.append(Chip)
        self.balance -= Chip.nominal

        login = f"-----Игрок {self.player_id} купил фишку {Chip.color}-----"
        print(login)
        log.log_in(login)
        return self.balance

        
    def GetMoney(self):
        return self.balance


    def LooseMoney(self, money):
        login = f"-----Игрок {self.player_id} потерял {money} рублей-----"
        print(login)
        log.log_in(login)
        self.balance -= money
        return self.balance


