from app.players.elves import elf


class Druid(elf.Elf):
    def __init__(
            self,
            nickname: str,
            favourite_spell: str,
            musical_instrument: str
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. "
                f"{self.nickname} has a favourite spell: "
                f"{self._favourite_spell}")

    def get_rating(self) -> int:
        return len(self._favourite_spell)
