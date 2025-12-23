# from src import log

class ChipNominals:
    def __init__(self):
        self._Color_Nominals = {}

    
    def __setitem__(self, color: str, nominal: int):
        self._Color_Nominals[color]=nominal 
        login = f'===== ОПРЕДЕЛЕНА НОВАЯ ФИШКА. ЦВЕТ: {color}, НОМИНАЛ: {nominal} ====='
        # log.log_in(login)
        return
    

    def GetNominal(self, color):
        return self._Color_Nominals[color]
    

    def __iter__(self):
        return iter(self._Color_Nominals)
    

    def __getitem__(self, key: str):
        return self._Color_Nominals[key]
    

    def values(self):
        return self._Color_Nominals.values()


    def value(self, obj):
        return self._Color_Nominals[obj]


    def __str__(self):
        return str(self._Color_Nominals)
    