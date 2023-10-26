from src.game_rules import DataStorage


class CloudDataStorage(DataStorage):
    def save_hp(self, hp: int) -> None:
        print(f"Saving hp to cloud: {hp}")

    def save_score(self, score: int) -> None:
        print(f"Saving score to cloud: {score}")


class LocalDataStorage(DataStorage):
    def save_hp(self, hp: int) -> None:
        print(f"Saving hp to local storage: {hp}")

    def save_score(self, score: int) -> None:
        print(f"Saving score to local storage: {score}")
