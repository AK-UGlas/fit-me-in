import unittest
from models.location import Location

class TestLocation(unittest.TestCase):
    def setUp(self):
        self.spin_room = Location("spin room", 10)
        self.tiny_room = Location("wee room", 3)

    