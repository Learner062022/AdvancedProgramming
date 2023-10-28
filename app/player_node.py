from player import Player


class PlayerNode:
    def __init__(self, _player: str):
        self._player = _player
        self._prev = None
        self._next = None

        # why may every instance variable not need a setter and what 1?

    @property
    def prev_node(self) -> None:
        return self._prev

    @prev_node.setter
    def prev_node(self, value):
        self._prev = value

    @property
    def next_node(self):
        return self._next

    @next_node.setter
    def next_node(self, value):
        self._next = value

    @property
    def key(self) -> property:
        return Player.uid

    def __str__(self) -> str:
        return f'{self._player}'

