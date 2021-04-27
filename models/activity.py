class Activity():
    def __init__(self, name, start_time, location, duration=60, id=None):
        self.name = name
        self.start = start_time
        self.location = location
        self.duration = duration
        self.id = id
