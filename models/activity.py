class Activity():
    def __init__(self, name, start_time, duration, location, date, id=None):
        self.name = name
        self.start = start_time
        self.duration = duration
        self.location = location
        self.date = date
        self.id = id
