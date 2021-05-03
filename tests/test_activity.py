import unittest, datetime
from models.activity import Activity
from models.location import Location

class TestActivity(unittest.TestCase):
    def setUp(self):
        self.now = datetime.datetime.now()
        deltas = [datetime.timedelta(minutes=60*hour) for hour in range(2, 10, 2)]
        self.tiny_room = Location("wee room", 3)
        self.yoga = Activity("yoga", start_time=self.now, location=self.tiny_room)

# test attributes

    def test_activity_has_name(self):
        self.assertEqual("yoga", self.yoga.name)

    def test_activity_has_start_time(self):
        self.assertEqual(self.now, self.yoga.start)

    def test_activity_has_location(self):
        self.assertEqual(self.tiny_room, self.yoga.location)

    def test_activity_id_is_none(self):
        self.assertEqual(None, self.yoga.id)
    
# test methods

    def test_return_date_as_iso8601_format_string(self):
        self.assertEqual(self.now.date().isoformat(), self.yoga.get_date(iso=True))

    def test_return_time_as_iso8601_format_string(self):
        self.assertEqual(self.now.time().isoformat(), self.yoga.get_start_time(iso=True))


        
