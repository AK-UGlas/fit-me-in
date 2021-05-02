import unittest, datetime
from models.activity import Activity
from models.location import Location

class TestActivity(unittest.TestCase):
    def setUp(self):
        now = datetime.datetime.now()
        deltas = [datetime.timedelta(minutes=60*hour) for hour in range(2, 10, 2)]
        self.tiny_room = Location("wee room", 3)
        self.yoga = Activity("yoga", start_time=now, location=self.tiny_room)

# test attributes

    def test_activity_id_is_none(self):
        self.assertEqual(None, self.yoga.id)

    
        
