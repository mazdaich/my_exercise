from dataclasses import dataclass, field


@dataclass(order=True)
class FootballPlayer():
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)


@dataclass(order=True)
class FootballTeam():
    name: str
    players: list = field(default_factory=list, repr=False, compare=False)

    def add_players(self, *args):
        for i in args:
            self.players.append(i)


if __name__ == '__main__':

    player = FootballPlayer('Kylian', 'Mbappe', 180000000)

    print(player)
    print(player.name)
    print(player.surname)
    print(player.value)
