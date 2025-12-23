class Person:
    def __init__(self, balance = 0, chips = {}):
        self.balance = balance
        self.chips = chips
        
class Goose:
    def __init__(self, name, balance):
        self.name = name
        self.volume = volume
        
class WarGoose(Goose):
    def __init__(self, power):
        self.power = power
        
class HonkGoose(Goose):
    def __init__(self, volume=10):
        self.volume = volume
        
        
    def scream(self):
        return
        
        
class CasinoBalance:
    def __init__(self):
        self._bank = {}
    
    
    def __len__(self):
        return len(self._bank)
        
    #Метод должен выбрасывать исключение TypeError, если используется некорректный тип ключа, KeyError, если данному ключу не соответствует ни один элемент в последовательности.
    def __getitem__(self, key: str):
        return self._bank[key]
        
    
    def __setitem__(self, key: str, value: int):
        self._bank[key] = value
        return
        
        
    def __iter__(self):
        return iter(self._bank)
        
        
Casic = CasinoBalance()
Casic["1"] = 1
Casic["2"] = 2
Casic["3"] = 3

print(len(Casic), Casic["2"])
for key, value in Casic:
    print (key, value)