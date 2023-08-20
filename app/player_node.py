from player import Player


class PlayerNode:
    def __init__(self, player):
        self._curr_node = player
        self._prev_node = None
        self._next_node = None

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, value):
        self._prev_node = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        self._next_node = value

    @property
    def key(self) -> property:
        return Player.uid

    def __str__(self) -> str:
        return f'{self._prev_node} <- {self._curr_node} -> {self._next_node}'
