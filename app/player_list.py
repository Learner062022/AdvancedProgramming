class PlayerList:

    def __init__(self, _head: None, _tail: None):
        self._head = _head
        self._tail = _tail  # Will this require a property

    def insert_node_at_head(self):  # Update _tail after inserted. Create
        if self.is_empty():
            ...
        else:
            ...

    def is_empty(self) -> bool:
        ...

    def insert_node_at_tail(self, node):
        if self.is_empty():
            ...
        else:
            ...

    def del_node_at_tail(self):
        ...

    def del_node_at_head(self):
        ...

    def del_node_via_key(self):
        ...
