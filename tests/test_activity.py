import unittest
from datetime import date
from models.activity import Activity
from models.location import Location

class TestActivity(unittest.TestCase):
    def setUp(self):
        self.yoga = Activity("yoga", )
        self.tiny_room = Location("wee room", 3)
