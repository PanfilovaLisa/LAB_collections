from src import const, log

class Goose:
    """
    Обычный гусь.

        self.goose_id - идентификатор гуся. Определяется автоматически из переменной const.GOOSE_ID
        self.balance - баланс гуся. Гусь создаётся с нулевым балансом
    """
    def __init__(self, goose_id="G" + str(const.GOOSE_ID), balance=0):
        self.goose_id = "G" + str(const.GOOSE_ID)
        self.balance = balance

    
    def StealMoney(self, money):
        """
        Гусь крадёт деньги -> зачисляет их себе на баланс
        """
        login = f"-----Гусь {self.goose_id} украл {money} рублей-----"
        print(login+"\n")
        # log.log_in(login)
        self.balance += money 
        return self.balance
    


class WarGoose(Goose):
    """
    Боевой гусь, наследуется от обычного гуся

        self.goose_id - идентификатор гуся. 'W' - боевой гусь.
        self.power - сила гуся

    """
    def __init__(self, power, goose_id="W" + str(const.GOOSE_ID), balance=0,):
        super().__init__(balance=balance)
        self.goose_id="W" + str(const.GOOSE_ID) 
        self.power = power


    def Attack(self, player):
        """
        Атака
            player - игрок для атаки. Объект класса Player.
        """
        money_for_steal = self.power*10
        player.LooseMoney(money_for_steal)


    def __add__(self, AnotherGoose):
        return self.power + AnotherGoose.power



class HonkGoose(Goose):
    def __init__(self, Honk_volume, goose_id="H" + str(const.GOOSE_ID), balance=0,):
        super().__init__(balance=balance)
        self.goose_id="H" + str(const.GOOSE_ID)
        self.honk_volume = Honk_volume
    

    def __call__(self):
        login = f"-----Вызван гусь {self.goose_id}-----"
        print(login)
        log.log_in(login)
        money_for_stole = self.honk_volume*100
        # self.StealMoney(money_for_stole)
        return money_for_stole
    