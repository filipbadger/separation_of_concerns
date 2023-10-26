from src.data_storage import CloudDataStorage
from src.game_rules import GameRules


data_storage = CloudDataStorage()
game = GameRules(data_storage)

# game.play()
game.damage_player()
