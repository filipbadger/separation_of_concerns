from dataclasses import dataclass
from typing import Protocol


class DataStorage(Protocol):
    def save_hp(self, hp: int) -> None:
        raise NotImplementedError

    def save_score(self, score: int) -> None:
        raise NotImplementedError


@dataclass
class Player:
    hp: int
    score: int


class GameRules:
    def __init__(self, data_storage: DataStorage) -> None:
        self._data_storage = data_storage
        self._player = Player(hp=100, score=0)

    def damage_player(self) -> None:
        self._player.hp -= 10
        self._data_storage.save_hp(self._player.hp)
