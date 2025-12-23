from src.animals import human
from src.casinobuild import casino

def CreatePlayer():
    player = human.Player()
    casino.Casino.AddPlayer(player_id=player.player_id)
    return