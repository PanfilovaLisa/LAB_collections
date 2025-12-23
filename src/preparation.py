from src.casinobuild import ceils
import random

def AddPlayers(Simulator):
    # СОЗДАНИЕ СТАРТОВОГО НАБОРА ИГРОКОВ
    for count in range (10):
        Simulator.CreatePlayer()
    return 


def AddGeese(Simulator):
    # Генерация обычных гусей
    for count in range (3):
        Simulator.CreateGoose(type=0)

    # Генерация боевого гуся
    Simulator.CreateGoose(type=1)

    # Генерация кричащего гуся
    Simulator.CreateGoose(type=2)
    return 


def CreateChips(CHIPS):
    CHIPS['white'] = 10
    CHIPS['res'] = 50
    CHIPS['green'] = 250
    CHIPS['blue'] = 500
    CHIPS['black'] = 1000


def CreateCeils(CEILS):
    B1 = ceils.Ceil('B1')
    B0 = ceils.Ceil('B0')
    R0 = ceils.Ceil('R0')
    R1 = ceils.Ceil('R1')

    CEILS.append(B0)
    CEILS.append(B1)
    CEILS.append(R0)
    CEILS.append(R1)


def PlayersBuyChips(Simulator, players):
    for player in players:
        Simulator.Casino.PlayerBuyChip(player)
    return
