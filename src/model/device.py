from schedule import Schedule

class Device:

    def __init__(self, id):
        self.id = id
        self.state = False
        self.scheduleList = []

    def on(self):
        self.state = True

    def off(self):
        self.state = False

    def addSchedule(self, schedule):
        self.scheduleList.append(schedule)
