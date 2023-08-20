import unittest
from app.player import Player
init_player = Player('1', 'D')
other_player = Player('2', 'D')


class TestPlayerProperties(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(len(init_player.uid), 0)

    def test_uniqueness(self):
        self.assertNotEqual(init_player.uid, other_player.uid)


if __name__ == '__main__':
    unittest.main()
