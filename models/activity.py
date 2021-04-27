import datetime

class Activity():
    def __init__(self, name, start_time, location, id=None):
        self.name = name
        self.start = start_time
        self.location = location
        self.duration = 60
        self.id = id

    def get_start_time(self, iso=False):
        time = self.start.time()
        if iso:
            return time.isoformat()
        return time.strftime("%H:%M")

    def get_date(self):
        return self.start.date().isoformat()
