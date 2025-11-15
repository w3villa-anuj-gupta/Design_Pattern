
# Observer Pattern : AnnouncementService

class AnnouncementService:
    def __init__(self):
        self.observers = []
    def subscribe(self, observer):
        self.observers.append(observer)
    def unsubscribe(self, observer):
        self.observers.remove(observer)
    def announce(self, message):
        for obs in self.observers:
            obs.notify(message)

class EmployeeObserver:
    def __init__(self, name):
        self.name = name
    def notify(self, message):
        print(f"{self.name} received: {message}")
