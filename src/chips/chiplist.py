from src.chips import chip

class ChipList:
    def __init__(self):
        self._CHIPLIST = []

    
    def append(self, chip):
        '''
        Добавление фишки в список. Так как данная функция определена только для 
        фишек, то список автоматически сортируется по возрастанию номинала фишки.
        '''
        self._CHIPLIST.append(chip)
        self._CHIPLIST.sort(key=lambda x: x.nominal)
        return
    

    def remove(self, el):
        return self._CHIPLIST.remove(el)


    def __iter__(self):
        return iter(self._CHIPLIST)


    def __str__(self):
        return str(self._CHIPLIST)