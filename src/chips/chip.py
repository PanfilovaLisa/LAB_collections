from src.chips import chips_nominals

class Chip:
    def __init__(self, CHIPS, color):
        self.color = color
        self.nominal = CHIPS.GetNominal(color)

    
    def __add__(self, other):
        return self.nominal + other.nominal