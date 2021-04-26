import unittest
from models.location import Location

class TestLocation(unittest.TestCase):
    def setUp(self):
        self.spin_room = Location("spin room", 10)
        self.tiny_room = Location("wee room", 3)

    def test_room_id_is_none(self):
        self.assertTrue(self.spin_room.id == None)

    def test_room_has_name(self):
        self.assertEqual("spin room", self.spin_room.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.spin_room.capacity)