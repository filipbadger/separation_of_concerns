from src.data_storage import LocalDataStorage
from src.game_rules import GameRules


data_storage = LocalDataStorage()
game = GameRules(data_storage)

# game.play()
game.damage_player()
