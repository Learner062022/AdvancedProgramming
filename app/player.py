class Player:
    _ids = list()

    def __init__(self, _id: str, _name: str):
        self._name = _name
        self._id = _id

    @property
    def uid(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return f'{self._id} is {self._name}'
