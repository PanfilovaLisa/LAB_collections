from src import log

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
        if 'P' in key:
            login = f"-----Баланс игрока {key} изменён. Баланс: {value}-----"
        elif any(key_letter in key for key_letter in 'GHW'):
            login = f"-----Баланс гуся {key} изменён. Баланс: {value}-----"
        elif 'B' in key:
            log.log_in(f"-----БАЛАНС КАЗИНО ОБНОВЛЕН. БАЛАНС КАЗИНО {value}-----")
            return
        print(login+"\n")
        log.log_in(login)
        return
        
        
    def __iter__(self):
        return iter(self._bank)
    

    def __str__(self):
        return str(self._bank)