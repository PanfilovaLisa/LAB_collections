from src.casinobuild import round, ceils
from src.collections import geese, balance, players
from src.chips import chip
from src import log
import random


class Casino:
    def __init__(self, CHIPS: dict, CEILS: list):
        self.PlayersCollection = players.PlayerCollection()
        self.GeeseCollection = geese.GooseCollection()
        self.CasinoBank = balance.CasinoBalance()
        self.CasinoBank['B'] = 0
        self.CEILS = CEILS
        self.CHIPS = CHIPS 


    def PlayRound(self):
        self.MakeBets()

        WinCeil = self.CEILS[random.randint(0, 3)]
        login = f"=====Выиграла ячейка {WinCeil.name}====="
        print(login+"\n")
        log.log_in(login)

        self.CollectLoss(WinCeil)

        self.PayWinning(WinCeil)


    def PayWinning(self, WinCeil):
        for player, bet in WinCeil:
            win = chip.Chip(color = bet.color, CHIPS=self.CHIPS)
            login = f"-----Игрок {player.player_id} выиграл {win.color} фишку-----"
            log.log_in(login)
            print(login)

            self.CasinoBank['B']-=win.nominal
            player.ChipList.append(bet)
            player.ChipList.append(win)
        WinCeil.clear()


    def CollectLoss(self, WinCeil):
        for ceil in self.CEILS:
            if ceil!=WinCeil:
                for player, bet in ceil.bets:
                    money = bet.nominal
                    self.CasinoBank['B']+=money 
                ceil.clear()

    
    def MakeBets(self):
        """
        Игроки делают ставки.

        Случайным образом определяется ячейка для ставки. Размер ставки - максимально имеющаяся у игрока фишка.

        """
        for player in self.PlayersCollection:
            if len(player.ChipList)>0:
                ceil_index = random.randint(0, 3)
                ceil = self.CEILS[ceil_index]
                bet = max(player.ChipList, key=lambda x: x.nominal)
                player.ChipList.remove(bet)
                ceil.bets.append((player, bet))

        for ceil in self.CEILS:
            for player, bet in ceil:
                login = f"-----Игрок {player.player_id} поставил {bet.color} фишку на ячейку {ceil.name}-----"
                print(login)
                log.log_in(login)
            print("\n")

    
    def PlayerBuyChip(self, player):
        player_balance = player.BuyChip(self.CHIPS)
        self.CasinoBank[player.player_id] = player_balance
        return

    
    def RenewCasinoBalance(self, money):
        bank = self.CasinoBank['B']
        self.CasinoBank['B'] = bank+money
        return


    def RenewPlayerBalance(self, money, player):
        balance=self.CasinoBank[player.player_id]
        self.CasinoBank[player.player_id]=money
        return 
    
    
    def RenewGooseBalance(self, money, goose):
        balance=self.CasinoBank[goose.goose_id]
        self.CasinoBank[goose.goose_id]=money 
        return

    def AddPlayer(self, player):
        self.PlayersCollection.append(player)
        print(f"-----Зарегестрирован игрок No {player.player_id}-----")
        self.CasinoBank[player.player_id] = player.balance
        return
    

    def AddGoose(self, goose):
        print(f"-----Зарегестрирован гусь No {goose.goose_id}-----")
        if 'G' in goose.goose_id:
            self.GeeseCollection[0].append(goose)
        elif 'W' in goose.goose_id:
            self.GeeseCollection[1].append(goose)
        else:
            self.GeeseCollection[2].append(goose)
        self.CasinoBank[goose.goose_id] = goose.balance
        return
    

    def CallHonkGoose(self, goose, player):
        money_for_stole = goose(player)
        self.RenewPlayerBalance(player=player, money=player.LooseMoney(money_for_stole))
        self.RenewGooseBalance(goose=goose, money=goose.StealMoney(money_for_stole))
        return
    

    def CheckPlayers(self):
        for player in self.PlayersCollection:
            if self.CasinoBank[player.player_id]<0:
                print(f"-----Игрок {player.player_id} влез в долги-----")
                self.GeeseAttack(player)
                login = f"-----ИГРОК {player.player_id} ВЫГНАН ЗА ДОЛГИ-----"
                self.PlayersCollection.remove(player)
                print(login)
                log.log_in(login)
        return


    def GeeseAttack(self, player):
        geese=self.GeeseCollection[1].copy()

        common_power = self.GeeseCollection.SumPower()
        money=common_power*50
        
        self.RenewPlayerBalance(player=player, money=player.LooseMoney(money))
        self.RenewCasinoBalance(money)
        return